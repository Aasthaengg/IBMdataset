a,b=map(int,input().split())

ans=[]

if b==1:
  print('0')

else:
  for i in range(20):
    if b<=a+(a-1)*i:
      ans.append(i+1)
  print(min(ans))