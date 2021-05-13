N=int(input())
L=[list(map(int,input().split())) for _ in range(N)]
L.sort(key=lambda x:x[1])
t=0
p=True
for l in L:
  t+=l[0]
  if t > l[1]:
    p=False
    break
print("Yes" if p else "No")