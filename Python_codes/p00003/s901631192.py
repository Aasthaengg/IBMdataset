import math

N = int(input())

for i in range(N):
  side_len = list(map(int, input().split(" ")))
  side_len.sort()
  if int(math.pow(side_len[0], 2)) + int(math.pow(side_len[1], 2)) == int(math.pow(side_len[2], 2)):
    print("YES")
  else:
    print("NO")
