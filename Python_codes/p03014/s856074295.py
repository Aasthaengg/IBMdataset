h,w = map(int,input().split())
S = [input() for _ in range(h)]
C = [[0 for _ in range(w)] for _ in range(h)]
for i in range(h):
    new = []
    flag = False
    cnt = 0
    for j in range(w):
        if flag:
            if S[i][j] == "#":
                for k in new:
                    C[i][k] += cnt
                cnt = 0
                new = []
                flag = False
            else:
                cnt += 1
                new.append(j)
        else:
            if S[i][j] == ".":
                cnt = 1
                flag = True
                new.append(j)
    else:
        if flag:
            for k in new:
                C[i][k] += cnt
            cnt = 0
            flag = False
for j in range(w):
    new = []
    flag = False
    cnt = 0
    for i in range(h):
        if flag:
            if S[i][j] == "#":
                for k in new:
                    C[k][j] += cnt
                cnt = 0
                new = []
                flag = False
            else:
                cnt += 1
                new.append(i)
        else:
            if S[i][j] == ".":
                cnt = 1
                flag = True
                new.append(i)
    else:
        if flag:
            for k in new:
                C[k][j] += cnt
            cnt = 0
            flag = False
ans = -1
for i in range(h):
    ans = max(ans,max(C[i]))
print(ans-1)