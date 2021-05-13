def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)
    divisors.sort()
    return divisors

n=int(input())
a=list(map(int,input().split()))
cnt=[0]*n
ans=[]
d={}
for i in range(n,0,-1):
  flag=False
  for j in make_divisors(i):
    if a[i-1]==1 and cnt[i-1]%2==0:
      cnt[j-1]+=1
      flag=True
    elif a[i-1]==0 and cnt[i-1]%2==1:
      cnt[j-1]+=1
      flag=True
  if flag:
    ans.append(i)
print(len(ans))
print(*ans)