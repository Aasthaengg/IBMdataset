k,a,b=map(int,input().split())
cnt=0
bis=1
yen=0
if b-a<3 or a>=k: print(1+k); exit()
if a>1:
  bis=a
  cnt=a-1
if k-cnt>1:
  bis=bis+(b-a)*((k-cnt)//2)
  if (k-cnt)%2==1: bis+=1
print(bis)