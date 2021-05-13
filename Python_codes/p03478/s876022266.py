N,A,B = input().split()
N,A,B = map(int,(N,A,B))
f=0
for i in range(1,N+1):
  k=i
  a = i//10000
  i = i-a*10000
  b = i//1000
  i = i-b*1000
  c = i//100
  i = i-c*100
  d = i//10
  i = i-d*10
  e = i
  s = a+b+c+d+e
  if A<=s<=B:
    f += k
print(f)

