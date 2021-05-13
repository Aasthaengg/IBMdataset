s=list(map(int, input().split()))
n=s[0]
a=s[1:]
l=[int(input()) for i in range(n)]
num=4**n
ans=1000000000
for i in range(num):
  t=i
  use=[[] for _ in range(4)]
  for j in range(n):
    use[t%4].append(l[j])
    t//=4
  cost=0
  for j in range(3):
    if len(use[j])==0:
      cost=100000000000
    else:
      cost+=(len(use[j])-1)*10+abs(sum(use[j])-a[j])
  ans=min(ans,cost)
print(ans)