import sys

n, m = map(int, input().split())

#偶数+偶数
result = n * (n - 1) // 2
#奇数+奇数
result += m * (m - 1) // 2
print(result)
