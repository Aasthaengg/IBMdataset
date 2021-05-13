x,a,b=map(int,input().split())	

l_1=abs(x-a)
l_2=abs(x-b)

if l_1<l_2:
  print('A')
else:
  print('B')