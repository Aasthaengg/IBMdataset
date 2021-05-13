N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
nega=0
posi=0
yoyu=[]
ans=0
for i in range(N):
  tmp=A[i]-B[i]
  if tmp>=0:
    posi+=tmp
    yoyu.append(tmp)
  else:
    nega+=-1*tmp
    ans+=1
if posi<nega:
  print(-1)
  exit()
elif nega==0:
  print(0)
  exit()

yoyu.sort(reverse=True)
S=0
i=0
while (1):
  S+=yoyu[i]
  if nega<=S:
    ans+=i+1
    print(ans)
    break
  else:
    i+=1