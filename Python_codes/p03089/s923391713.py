n=int(input())
a=[]
b=list(map(int,input().split()))
for i in range(n):
  for j in range(n)[n-i-1::-1]:
    if b[j]==j+1:
      a.append(b.pop(j))
      break
if len(a)<n:
  print(-1)
  exit()
a.reverse()
for i in a:
  print(i)