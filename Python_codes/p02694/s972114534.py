X = int(input())
c = 100
ret = 0
while c < X:
  ret += 1
  c = c * 101 // 100

print(ret)