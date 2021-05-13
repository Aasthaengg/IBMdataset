a,b=map(int,input().split())
ans=[]

for i in range(50):
  l=[]
  for j in range(100):
    if i%2==0 and j%2==0 and a>1:
      l.append('.')
      a-=1
    else:
      l.append('#')
  ans.append(l)

for i in range(50):
  l=[]
  for j in range(100):
    if i%2==1 and j%2==1 and b>1:
      l.append('#')
      b-=1
    else:
      l.append('.')
  ans.append(l)

print(100,100)
for i in range(100):
  print(''.join(ans[i]))