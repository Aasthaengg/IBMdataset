num_500 = int(input())
num_100 = int(input())
num_50 = int(input())
ans = int(input())

resultCnt = 0

for i in range(num_500+1):
  for j in range(num_100+1):
    for k in range(num_50+1):
      if 500*i + 100*j + 50*k == ans:
        resultCnt += 1

print(resultCnt)