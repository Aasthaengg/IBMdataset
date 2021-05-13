n=int(input())
s=[i for i in range(1,n+1)]
sum=0
for i in range(n):
  if s[i]%2!=0:
    sum=sum+1
print(sum/n)
