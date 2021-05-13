def cin():  return list(map(int,input().split()))

N = cin()[0]
a = cin()

ans = [0] * N
cnt = a[0]
tmp = 1
for i in range(1, N):
    tmp *= -1
    cnt += a[i] * tmp
ans[0] = cnt
for i in range(1, N):  ans[i] = 2 * a[i - 1] - ans[i - 1]
print(*ans)