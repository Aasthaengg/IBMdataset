# 1,2,3
# 01
# 10
# 11

# 両隣のXORと一致->両隣と自分をXORすると0になる
# 連続した3つのXORが0になる
# a,b,c,dでaとdは同じになる

# 円環になるには、
# a,b,c,a,b,cというセットになり、
# 且つa,b,cのXORが0であればよい

# もしくは全部0

# もしくはa,a,0,a,a,0

n=int(input())
a=list(map(int,input().split()))
dis=set(a)
if a[0]==0 and len(dis)==1:
  print("Yes")
  exit(0)
if len(dis)==3:
  xor=0
  cur=0
  for c in dis:
    xor^=c
    cnt=a.count(c)
    if cur==0:
      cur=cnt
    else:
      if cnt!=cur:
        print("No")
        exit(0)
  if xor==0:
    print("Yes")
    exit(0)
if len(dis)==2:
  if a.count(0)==n//3 and n%3==0:
    print("Yes")
    exit(0)
print("No")