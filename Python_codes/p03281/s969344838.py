ans=0
n=int(input())
if n<105:
  print('0')
  exit()
else:
  for i in range(105,n+1):
    if i%2!=0:
      cnt=0
      for j in range(1,i+1):
        if i%j==0:
          cnt+=1
      if cnt==8:
         ans+=1

print(ans)