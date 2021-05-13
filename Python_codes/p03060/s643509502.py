n=int(input())
s=list(map(int,input().split()))
c=list(map(int,input().split()))

count=0
for i in range(n):
  if s[i]>c[i]:
    count=s[i]-c[i]+count
    
print(count)