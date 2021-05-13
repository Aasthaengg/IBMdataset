import math
A,B,N = map(int, input().split())

# 0,1,2..B-1 毎の繰り返しとなる
# Nの範囲で、最大はB-1が最大となるので、 min(N, B-1)

x = min(N, B-1)
ans = math.floor(A*x/B) - A*math.floor(x/B)
print(ans)
