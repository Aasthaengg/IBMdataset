a,b,c,k = map(int,input().split())
sum = 0
if k%2==0:
  sum = a-b
else:
  sum = b-a
if abs(sum)>=10**18:
  print("Unfair")
else:
  print(sum)