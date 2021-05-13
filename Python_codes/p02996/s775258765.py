from sys import exit
N = int(input())
L = []
for _ in range(N):
  L.append(list(map(int, input().split())))
L.sort(key=lambda  x: x[1])
used = 0
for l in L:
  used += l[0]
  if used > l[1]:
    print("No")
    exit()
print("Yes")