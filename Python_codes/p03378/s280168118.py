N,M,X = map(int,input().split())
A = list(map(int,input().split()))

left = sum(x<X for x in A) 
right = sum(x>X for x in A)  

if left <= right:
  print(left)
else:
  print(right)