k=int(input())
a=list(map(int,input().split()))
if a[-1]!=2:
  print(-1)
  exit()
l,r=2,2
for i in range(k):
  ai=a[-1-i]
  # l以上r以下のaiの倍数を探す。なければ-1
  if r<ai or (l//ai==r//ai and l%ai!=0):
    print(-1)
    exit()
  l=ai*((l+ai-1)//ai)
  r=ai*(r//ai)+(ai-1)
print(l,r)

