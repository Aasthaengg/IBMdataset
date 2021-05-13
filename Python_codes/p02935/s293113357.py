n=int(input())
v=list(map(int,input().split()))
v.sort(key=int)
for i in range(n-1):
  z=(v[i]+v[i+1])/2
  v[i]=z
  v[i+1]=z
print(v[n-1])
