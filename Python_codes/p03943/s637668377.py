a,b,c = map(int,input().split())
n = [a,b,c]
abc = (a+b+c)/2
if abc in n:
  print("Yes")
else:
  print("No")