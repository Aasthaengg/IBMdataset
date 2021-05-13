N,x = map(int, input().split())
A = sorted(map(int, input().split()))
s = 0
for i in range(N):
  x -= A[i]
  if x<0:
    break
  else:
    s += 1
print(s if x<=0 else s-1)