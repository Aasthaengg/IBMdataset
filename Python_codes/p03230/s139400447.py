n=int(input())
k=int((n*2)**0.5)
if (k*(k+1))//2==n:
  print('Yes')
  print(k+1)
else:
  print('No')
  exit()
s=[[] for _ in range(k+1)]
t=1
for i in range(1,k+1):
  for j in range(i):
    s[i].append(t)
    s[j].append(t)
    t+=1
for i in s:
  print(len(i),*i)
