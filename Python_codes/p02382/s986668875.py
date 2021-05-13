import math

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(sum([abs(a[i] - b[i]) for i in range(n)]))
print(pow(sum([abs(a[i] - b[i]) **2 for i in range(n)]), 1/2))
print(pow(sum([abs(a[i] - b[i]) **3 for i in range(n)]), 1/3))
print(max([abs(a[i] - b[i]) for i in range(n)]))

