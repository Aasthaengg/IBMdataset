n,t=map(int,input().split())
a=list(map(int,input().split()))
v=[[a[0],a[0]+t]]
for i in a[1:]:
  if i<=v[-1][1]:v[-1][1]=i+t
  else:v.append([i,i+t])
print(sum(j-i for i,j in v))