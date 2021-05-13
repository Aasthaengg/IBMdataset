K, A, B = map(int, input().split())
if A+2 >= B or A >= K:
  print(K+1)
else:
  print(B + ((K-A+1)//2-1)*(B-A) + ((K-A+1)%2))