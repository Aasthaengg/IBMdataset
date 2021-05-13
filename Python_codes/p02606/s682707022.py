baseData = [int(i) for i in input().split(" ")]
L = baseData[0]
R = baseData[1]
d = baseData[2]

cnt = 0

for i in range(L,R + 1):
  if i % d == 0:
    cnt += 1

print(cnt)