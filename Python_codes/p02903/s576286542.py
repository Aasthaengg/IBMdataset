miis=lambda:map(int,input().split())

h,w,a,b=miis()
ans=[]
for i in range(b):
  ans.append(['1']*a+['0']*(w-a))
for i in range(h-b):
  ans.append(['0']*a+['1']*(w-a))
for i in ans:
  print(''.join(i))