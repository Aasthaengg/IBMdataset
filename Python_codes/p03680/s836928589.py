N = int(input())
A = [int(input())-1 for _ in range(N)]

light = 0
ans = -1
for n in range(1,N+1):
  light = A[light]
  if light ==1:
    ans = n
    break
print(ans)