N, T = map(int, input().split())
A = list(map(int, input().split()))

limit = 0
tmp = A[0]
for a in A[1:]:
   limit = max(limit, a - tmp)
   tmp = min(tmp, a)

ans = [0] * N
maximum = A[-1]
ans[-1] = maximum
for i in range(N - 2, -1, -1):
    ans[i] = maximum - limit #これより安くする必要がある
    maximum = max(maximum, A[i])

tmp = 0
for i in range(N - 1):
    tmp += max(0, ans[i] - A[i] + 1)

# print (A)
# print (ans)
print (tmp)