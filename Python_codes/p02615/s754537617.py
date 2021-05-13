N = int(input())
A = list(map(lambda x: int(x), input().split(' ')))
A.sort(reverse=True)
score = 0
for i in range(N - 1):
  score += A[(i + 1) // 2]
print(score)