N,A,B = map(int,input().split())

if B < A:
  print(0)
  exit()
num = B-A+1
mi = A*(N-1) + B
ma = B*(N-1) + A
ans = ma - mi + 1

print(max(ans,0))