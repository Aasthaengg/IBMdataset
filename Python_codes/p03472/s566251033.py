n,h=map(int,input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
a, b = [list(i) for i in zip(*ab)]
ab.sort(reverse=True)

bm=ab[0][1]
b.remove(bm)
b.sort()

c=0
while h>0:
  if h<=bm:
    c+=1
    break
  if len(b)>0:
    if b[-1]>ab[0][0]:
      h-=b.pop()
      c+=1
      continue
  c+=(h-bm-1)//ab[0][0]+2
  h=0

print(c)