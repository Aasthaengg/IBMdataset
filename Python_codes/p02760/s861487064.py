A = [list(map(int,input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for i in range(N)]
cnt = [0]*8
ans = "No"
for i in range(3):
    for j in range(3):
        if A[i][j] in b:
            cnt[i] += 1
            cnt[j+3] += 1
            if i == j:
                cnt[-1] += 1
            if i+j == 2:
                cnt[-2] += 1
for k in range(8):
    if cnt[k] >= 3:
        ans = "Yes"
        break
print(ans)