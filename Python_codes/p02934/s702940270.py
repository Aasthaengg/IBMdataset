n=int(input())
a=list(map(int,input().split()))

s=1
for i in a:
  s*=i
ans=s/sum(s/i for i in a)
print(ans)