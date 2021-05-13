K, A, B = map(int, input().split())
if A+2 > B:
  print(K+1)
else:
  print(A+max(0, (K-A+1)//2)*(B-A)+(K-A+1)%2)