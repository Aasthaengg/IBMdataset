n=int(input())
ans=0
lis=[]
def cnt(n):
  ret=0
  for i in range(1,n):
    ret+=i
  return ret
for i in range(n):
  lis.append(sorted(list(input())))
co=1
lis.sort()
bef=lis[0]

for i in lis[1:]:
  if bef!=i:
    ans+=cnt(co)
    co=1
    bef=i
  else:
    co+=1
ans+=cnt(co)
print(ans)