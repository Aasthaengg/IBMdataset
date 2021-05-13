n,m=map(int,input().split())
dic={}
if n==1 and m==0:
  print('0')
  exit()

for i in range(m):
  s,c=map(int,input().split())
  
  if s not in dic:
    if n==1 and s==1 and c==0:
      print('0')
      exit()
    elif s==1 and c==0:
      print('-1')
      exit()
    else:
      dic[s]=c
  elif dic[s]==c:
    continue
  else:
    print('-1')
    exit()

for i in range(1,n+1):
  if i==1 and i not in dic:
    print('1',end="")
  elif i in dic:
    print(dic[i],end='')
  else:
    print('0',end='')
