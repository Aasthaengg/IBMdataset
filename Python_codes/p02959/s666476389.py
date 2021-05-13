n = int(input())
monster = list(map(int, input().split()))
brave = list(map(int, input().split()))
res = 0
for i in range(n):
  temp = min(monster[i], brave[i])
  brave[i] -= temp
  res += temp
  temp = min(monster[i + 1], brave[i])
  monster[i + 1] -= temp
  res += temp
print(res)