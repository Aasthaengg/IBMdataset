N = int(input())
A = [0] + [int(input()) for i in range(N)]
if A[1] != 0:
  print(-1)
  quit()

ans = 0
for i, a in enumerate(A[1:], 1):
  pre_a = A[i-1]
  if a - pre_a >= 2:
    print(-1)
    quit()
  elif a > pre_a:
    ans += 1
  else:
    ans += a

print(ans)