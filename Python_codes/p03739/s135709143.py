N = int(input())
A = list(map(int, input().split()))

# 方針:正負正...と負正負...の両方を試す
ans = 0
now = 0
for i in range(N):
    if i % 2 == 0:# 正にする
        if now+A[i] <= 0:
            ans += 1 - (now+A[i])
            now = 1
        else:
            now += A[i]
    else:
        if now+A[i] >= 0:
            ans += 1 + (now+A[i])
            now = -1
        else:
            now += A[i]
ans2 = 0
now = 0
for i in range(N):
    if i % 2 == 1:# 正にする
        if now+A[i] <= 0:
            ans2 += 1 - (now+A[i])
            now = 1
        else:
            now += A[i]
    else:
        if now+A[i] >= 0:
            ans2 += 1 + (now+A[i])
            now = -1
        else:
            now += A[i]

print(min(ans,ans2))