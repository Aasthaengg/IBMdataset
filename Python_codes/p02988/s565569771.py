n = int(input()) - 2
L = list(map(int, input().split()))
a = 0

for i in range(n):
  if L[i] < L[i+1] and L[i+1] < L[i+2]:
    a = a+1
  elif L[i+2] < L[i+1] and L[i+1] < L[i]:
    a = a+1
    
print(a)