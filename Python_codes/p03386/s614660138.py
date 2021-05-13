A,B,K = map(int,input().split())

for a in range(A,min(A+K,B+1)):
  print(a)
for b in range(max(A+K,B-K+1),B+1):
  print(b)