n,m=map(int,input().split())

c=list(map(int,input().split()))

cash=[0 for i in range(n+1)]

for i in range(1,n+1):
  for j in range(m):
    if (i-c[j])>=0:
      coins=cash[i-c[j]]+1
      if cash[i]==0:
        cash[i]=coins
      elif cash[i]>coins:
        cash[i]=coins

print(cash[n])
