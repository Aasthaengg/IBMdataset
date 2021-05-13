a = int(input())#500
b = int(input())#100
c = int(input())#50
x = int(int(input())/50)

cnt = 0

for i in range(a + 1):
  for j in range(b + 1):
    for k in range(c + 1):
      s = int(i*10 + j*2 + k)
      if s == x:
        cnt += 1

print(cnt)