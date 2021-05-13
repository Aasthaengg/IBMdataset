n=int(input())
a=list(map(int,input().split()))
d=[0]
for i in range(1,n+1):
  d.append(a[i-1]*2-d[-1])
t=d[-1]/2
d=[t]
for i in range(1,n+1):
  d.append(a[i-1]*2-d[-1])
print(" ".join(map(lambda x:str(int(x)),d[:-1])))
