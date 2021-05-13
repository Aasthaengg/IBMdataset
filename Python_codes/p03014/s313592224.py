H, W = map(int, input().split())
S = []
for i in range(H):
    S.append(input())
    
ans_W = [[-1 for i in range(W)] for j in range(H)]
for i in range(H):
    count = 0
    now = 0
    for j in range(W):
        if S[i][j] == ".":
            count += 1
        else:
            for k in range(now, min(W, now+1+count)):
                if k == j:
                    ans_W[i][k] = 0
                else:
                    ans_W[i][k] = count
            now += count+1
            count = 0
    if count != 0:
        for k in range(now, min(W, now+1+count)):
            ans_W[i][k] = count

ans_H = [[-1 for i in range(W)] for j in range(H)]
for i in range(W):
    count = 0
    now = 0
    for j in range(H):
        if S[j][i] == ".":
            count += 1
        else:
            for k in range(now, min(H, now+1+count)):
                if k == j:
                    ans_H[k][i] = 0
                else:
                    ans_H[k][i] = count
            now += count+1
            count = 0
    if count != 0:
        for k in range(now, min(H, now+1+count)):
            ans_H[k][i] = count

ans = 0
for i in range(H):
    for j in range(W):
        ans = max(ans, ans_H[i][j] + ans_W[i][j])
            
print(ans-1)
