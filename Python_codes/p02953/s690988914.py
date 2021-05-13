N = int(input())
H = list(map(int,input().split()))

maxH = 0
for i in range(N-1):
  if H[i+1] >= maxH-1:
    maxH = max(maxH,H[i+1])
  else:
    print("No")
    exit()
    
print("Yes")