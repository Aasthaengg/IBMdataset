n= int(input())
x= list(map(int,input().split()))
m= sum(x)/len(x)
g= int(m)
ans=0
if m-g<g+1-m:
  ans=g
else:
  ans=g+1
aaa=0
for i in x:
  aaa+= (ans-i)**2
print(aaa)