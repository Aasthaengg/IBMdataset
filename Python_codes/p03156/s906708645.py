n = int(input())
a,b = map(int,input().split())
lis = list(map(int,input().split()))
pro1,pro2,pro3 = 0,0,0
for problem in lis:
  if problem <= a:pro1 += 1
  elif problem <= b:pro2 += 1
  else:pro3 += 1
print(min(pro1,pro2,pro3))