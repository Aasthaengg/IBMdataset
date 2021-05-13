n=int(input())
k=int(input())
t=1
for i in range(n):
  if t*2<=t+k:
    t=t*2
  else:
    t+=k
print(t)