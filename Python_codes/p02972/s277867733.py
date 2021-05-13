def divisors(n):
   d=[]
   for i in range(1,int(n**0.5)+1):
       if n%i==0:
           d.append(i)
           if i!=n//i:
               d.append(n//i)
   d.sort()
   return d
n=int(input())
table=[0]*(n+1)
ball=[]
a=list(map(int,input().split()))[::-1]
for i in range(n):
    if table[n-i]!=a[i]:
        ball.append(n-i)
        for j in divisors(n-i):
            table[j]=1-table[j]
print(len(ball))
if len(ball)!=0:
    print(*ball)