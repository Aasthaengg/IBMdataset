import sys

n = int(input())
ab = [list(map(int, input().split())) for i in range(n)]
time = 0
ab.sort(key=lambda x: x[1])
for i in ab:
  if time + i[0] > i[1]:
    print("No")
    sys.exit()
  else:
    time += i[0]
print("Yes")