a=int(input())
b=list(map(int,input().split()))
b.sort(reverse=True)
ans=0
for i in range(a-1):
  i=(i+1)//2
  ans+=b[i]
print(ans)