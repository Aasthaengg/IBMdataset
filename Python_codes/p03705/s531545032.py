n,a,b=map(int,input().split())
if a > b or (n==1 and a != b):
  # 該当パターンなし
  print(0)
else:
  print((b-a)*(n-2)+1)