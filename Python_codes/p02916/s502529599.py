n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))

bef=a[0]-1
man=b[bef]

for i in a[1:]:
  ind=i-1
  if ind==bef+1:
    man+=c[bef]
  man+=b[ind]
  bef=ind
print(man)
