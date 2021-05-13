import collections 
n=input()
a=tuple(map(int,input().split()))
c=collections.Counter(a)
b=sorted(list(set(a)))[::-1]
ans,count=0,0
for i in b:
  if c[i]>3 and ans==0:
    print(i**2)
    exit()
  if c[i]>1:
    ans=ans*i if ans>0 else i
    count+=1
    if count==2:
      print(ans)
      exit()
print(ans)