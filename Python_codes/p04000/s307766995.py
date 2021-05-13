H,W,N = map(int,input().split())
dic={}
for _ in range(N):
  a,b = [int(x)-1 for x in input().split()]
  for h in range(a,a+3):
    for w in range(b,b+3):
      if 0<=h-2 and h<H and 0<=w-2 and w<W:
        dic[10**10*h+w] = dic.get(10**10*h+w,0)+1
ans = [0]*10
for x in dic.values():
  ans[x] += 1
ans[0] = (H-2)*(W-2)-sum(ans[1:])
for x in ans:
  print(x)
        
