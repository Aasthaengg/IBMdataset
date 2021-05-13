from itertools import accumulate
n = int(input())
a = list(map(int, input().split()))
l = list(accumulate(a))
x = 10 ** 10
for i in range(n-1):
    x = min(x, abs(l[i]*2-l[-1]))
print(x)