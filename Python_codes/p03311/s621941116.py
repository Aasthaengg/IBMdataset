n=int(input())
b=[int(a-(i+1))  for i,a in enumerate(list(map(int,input().split())))]
if n==1:
  print(0)
  exit(0)
bm=b[:]
bm.sort()
mid_1=bm[n//2]
mid_2=bm[(n//2)+1]
ans_1,ans_2=0,0
if n%2==1:
  for bb in b:
    ans_1+=abs(bb-mid_1)
  print(ans_1)
else:
  for bb in b:
    ans_1+=abs(bb-mid_1)
    ans_2+=abs(bb-mid_2)
  print(min(ans_1,ans_2))

