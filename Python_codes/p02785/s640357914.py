a,b=map(int,input().split())
l=sorted(list(map(int,input().split())))
z=0
for i in range(a-b):
  z+=l[i]
print(z)