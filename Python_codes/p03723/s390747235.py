a,b,c=map(int,input().split())
# 奇数があったら0回
if any([q%2==1 for q in (a,b,c)]):
  print(0)
  exit()
# 全部偶数で等しいと終わらない
if a==b==c:
  print(-1)
  exit()
# ではなければシミュレーションでOK
cnt=0
while all([q%2==0 for q in (a,b,c)]):
  cnt+=1
  s=a+b+c
  a=s-a
  a//=2
  b=s-b
  b//=2
  c=s-c
  c//=2
print(cnt)
