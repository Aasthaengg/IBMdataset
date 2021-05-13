z=list(map(int,input().split()))
a=z[0]//z[1]
if z[0]%z[1]!=0:
       a+=1
print(a)