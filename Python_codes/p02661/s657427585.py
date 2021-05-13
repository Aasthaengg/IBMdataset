n = int(input())
AB = []
A = [0]*n
B = [0]*n
for i in range(n):
  A[i],B[i] = map(int,input().split())  

A = sorted(A)  
B = sorted(B)  

if n%2 == 1:
  l = A[n//2]
  r = B[n//2]
  print(r-l + 1)
else:
  l = (A[n//2-1]+A[n//2])/2
  r = (B[n//2-1]+B[n//2])/2
  print(int((r-l)*2+1))