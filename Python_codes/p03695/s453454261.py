N = int(input())
A = list(map(int, input().split()))

ans = [0]*8
leng = 0

for i in range(N):
    now = A[i]//400
    if now < 8:
        ans[now] = 1
    else:
        leng += 1

mi = sum(ans) if sum(ans) > 0 else 1
print(mi, sum(ans) + leng)
