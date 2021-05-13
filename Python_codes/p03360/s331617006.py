a,b,c=map(int,input().split())
k=int(input())
temp=max(a,b,c)
for i in range(k):
  temp=temp*2
print(a+b+c+temp-max(a,b,c))
