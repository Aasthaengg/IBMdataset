a,b,c,d=map(int,input().split())
if -d<=a-c<=d or (-d<=a-b<=d and -d<=b-c<=d):
  print('Yes')
else:
  print('No')