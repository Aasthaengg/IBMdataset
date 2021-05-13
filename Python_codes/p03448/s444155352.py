A = int(input())
B = int(input())
C = int(input())
X = int(input())

cnt = 0

for a in range(A + 1):
  if 500 * a <= X:
    for b in range(B + 1):
      if 500 * a + 100 * b <= X:
        for c in range(C + 1):
          if 500 * a + 100 * b + 50 * c == X:
            cnt += 1
print(cnt)