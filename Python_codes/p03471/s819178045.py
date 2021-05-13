N, Y = map(int, input().split())
 
# 拘束条件を用い、探索をO(N^3)からO(N^2)へ！
a, b, c = -1, -1, -1
for i in range(0, N+1):
  for j in range(0, N+1-i):
    k = N - i - j
    if 10000*i + 5000*j + 1000*k == Y:
      a, b, c = i, j, k
  
print(a, b, c)