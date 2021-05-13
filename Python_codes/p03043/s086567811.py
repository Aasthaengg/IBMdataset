n, k = list(map(int, input().split()))

result = 0.0
for i in range(n):
  score = i + 1
  rate = 1.0
  while(score < k):
    rate = rate / 2
    score = score * 2
  result += rate

result = result / n
print(result)