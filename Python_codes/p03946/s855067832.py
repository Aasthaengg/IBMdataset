N,T=map(int,input().split())
A=list(map(int,input().split()))

d = 0
cnt = 0
min_a = A[0]
for i in range(1, N):
  a = A[i]
  if min_a > a:
    min_a = a
    continue
 
  if d < a - min_a:
    d = a - min_a
    cnt = 1
  elif d == a - min_a:
    cnt += 1
print(cnt)