A, B = list(map(int, input().split()))

if A < B:
  x = A
  y = B
  c = [".", "#"]
else:
  x = B
  y = A
  c = ["#", "."]
  
S = []

if x <= 50:
  y -= 1
elif x % 50 != 0:
  y += 50 - x % 50

cnt = 0
while x > 50:
  S.append([c[0] if (i + cnt) % 2 == 0 else c[1] for i in range(100)])
  x -= 50
  y -= 50
  cnt += 1

if x != 1:
  S.append([c[0] if (i + cnt) % 2 == 0 and i < (x - 1) * 2 else c[1] for i in range(100)])
  cnt += 1

S.append([c[1] for i in range(100)])
cnt += 1
S.append([c[0] for i in range(100)])
cnt += 1

while y >= 1:
  S.append([c[1] if (i + cnt * 2) % 4 == 0 and i < y * 4 else c[0] for i in range(100)])
  y -= 25
  cnt += 1
  
print(cnt, 100)
for i in S:
  print("".join(i))