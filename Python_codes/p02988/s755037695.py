# 132 B

n = int(input())
p = list(map(int, input().split()))
num = 0

def sec(a, k, b):
    if (a <= k <= b) or (a >= k >= b):
        global num
        num += 1

for i in range(1, n-1):
    sec(p[i-1], p[i], p[i+1])

print(num)