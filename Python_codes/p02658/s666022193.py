N=int(input())
s=list(map(int,input().split()))
ans=1
if s.count(0)>0:
  print('0')
  exit()
for i in s:
  ans*=i
  if ans>1000000000000000000:
    print('-1')
    exit()

print(ans)