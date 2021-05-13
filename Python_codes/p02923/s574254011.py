n=int(input())
h=list(map(int,input().split()))
c=0
t=0

for i in range(n-1):
  if h[i]>=h[i+1]:
    c+=1
  else:
    t=max(t,c)
    c=0
  t=max(t,c)
print(t)
