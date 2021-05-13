N = int(input())
H = list(map(int, input().split()))
H[0] -= 1
T = True
for i in range(1, N-1):
  if H[i-1]==H[i] and H[i]<=H[i+1]:
    continue
  elif H[i-1]<H[i] and H[i]-1<=H[i+1]:
    H[i] -= 1
    continue
  else:
    T = False
    break
print("Yes" if T else "No")
