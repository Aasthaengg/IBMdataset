A, B, K= map(int, input().split())

for i in range(A,min([A+K+1,B+1]),1):
  if i<A+K:
    print(i)
    
for i in range(max([A+K, B-K-1]),B+1,1):
  if i>B-K:
    print(i)