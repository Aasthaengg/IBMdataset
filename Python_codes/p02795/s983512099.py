h = int(input())
w = int(input())
n = int(input())

answer = h+w
for i in range(h+1):
  for j in range(w+1):
    area = i * w + j * h - i * j
    if area >= n:
      answer = min(answer, i+j)

print(answer)