N = int(input())
L = input().split()
max = 0
count = 0

for i in range(N):
  count += int(L[i])
  if max < int(L[i]):
    max = int(L[i])
    
if count > 2*max:
  print("Yes")
else:
  print("No")