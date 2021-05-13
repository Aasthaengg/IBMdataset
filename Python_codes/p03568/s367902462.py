N = int(input())
A = list(map(int, input().split()))
a = len(A)
t = 1 # odd

for i in range(N):
  if A[i] % 2 == 0:  
    t *= 2
  else: 
    t *= 1
print(3 ** a -t) 