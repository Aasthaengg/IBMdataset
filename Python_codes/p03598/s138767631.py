def calcdistance(N, K, x) : 
  sum = 0
  for i in range(N) : 
    sum += 2 * min(x[i] - 0, K - x[i])
  return sum

N = int(input())
K = int(input())
x = list(map(int, input().split()))

print(calcdistance(N, K, x))