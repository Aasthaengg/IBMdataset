n = int(input())
L = list(map(int, input().split()))
rep = []
for i in range(n):
  for j in range(n-1-i, -1, -1):
    if L[j] == j+1:
      rep.append(L.pop(j))
      break
  else:
    print(-1)
    exit()
print(*rep[::-1], sep="\n")