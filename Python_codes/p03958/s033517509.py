K,T=map(int,input().split())
a=list(map(int,input().split()))
b=[]

for i,an in enumerate(a):
    b.append([an,i])
ex = -1
ans = 0

if T == 1:
	print(K-1)
else:
  for i in range(K):
    list.sort(b, reverse=True)
    if ex == b[0][1] and b[1][0] != 0:
      b[1][0] -= 1
      ex = b[1][1]
      if b[0][1] == 0 and b[1][1] == 0:
        break
    else:
      b[0][0] -= 1
      if ex == b[0][1]:
        ans+=1
      ex = b[0][1]
      if b[0][1] == 0 and b[1][1] == 0:
        break
  print(ans)

