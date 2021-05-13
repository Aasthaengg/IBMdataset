N = int(input())
L = input().split()
flag = 0
total = 0

for i in range(N):
  L[i] = int(L[i])
  total += L[i]

for i in range(N):
  if L[i]*2 >= total:
    print("No")
    flag = 1
    break

if flag == 0:
  print("Yes")