N = int(input())
H = list(map(int,input().split()))
H.reverse()

check = True

for i in range(N-1):
  if H[i] >= H[i+1]:
    continue
  else:
    if H[i+1] - H[i] > 1:
      check = False
      break
    else:
      H[i+1] -= 1
      
if check:
  print("Yes")
else:
  print("No")