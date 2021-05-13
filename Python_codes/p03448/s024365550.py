A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0
for a in range(0,A+1):
  for b in range(0,B+1):
    c = (X - 500 * a - 100 * b) // 50
    if 0 <= c and c <= C:
      cnt += 1
      
print(cnt)