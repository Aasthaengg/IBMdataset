N = int(input())
H = list(map(int,input().split()))
safe = True
for i in reversed(range(N-1)):
  if H[i] > H[i+1]:
    H[i] -=1
for i in range(N-1):
  if H[i] > H[i+1]:
    safe = False
    break
print('Yes' if safe else 'No')