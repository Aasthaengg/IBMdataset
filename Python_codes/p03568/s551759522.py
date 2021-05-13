N = int(input())
A = list(map(int, input().split()))
even_cnt = []
for i in range(N):
  c = 0
  if A[i] % 2 == 0:
    even_cnt.append(1)
    A[i] = 2
  else:
    even_cnt.append(2)
    A[i] = 1

x = 3 ** N 
ans = 0
for i in range(N):
  x = x // 3
  ans += even_cnt[i] * x
  x *= A[i]
print(ans)