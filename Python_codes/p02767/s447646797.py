n=int(input())
x=list(map(int,input().split()))

min_=min(x)
max_=max(x)
ans=list()
for xy in range(min_, max_+1):
  life=0
  for xx in x:
    life+=(xx-xy)**2
  ans.append(life)
print(min(ans))