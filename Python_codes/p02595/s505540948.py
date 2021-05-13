N,D = map(int, input().split())
index = D**2
count = 0
for i in range(N):
  a,b = map(int,input().split())
  c = (a**2)+(b**2)
  if c<=index:
    count+=1

print(count)