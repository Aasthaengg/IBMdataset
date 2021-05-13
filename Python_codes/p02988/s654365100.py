N = int(input())
P = list(map(int,input().split()))
A = 0
for i in range(1, N-1):
    if P[i-1] < P[i] < P[i+1]: 
      A += 1
    if P[i-1] > P[i] > P[i+1]: 
      A += 1
print(A)