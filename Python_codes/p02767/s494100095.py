n=int(input())
x=[int(x) for x in input().split()]
ave1=sum(x)//n
ave2=ave1+1
a=0
b=0
for j in x:
  a+=(j-ave1)**2
  b+=(j-ave2)**2
print(min(a,b))