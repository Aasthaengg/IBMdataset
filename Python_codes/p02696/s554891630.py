import math
a, b, n = map(int,input().split())
# N = int(input())
# al = list(map(int,input().split()))

lst = []
if b > n:
    x = n
else:
    x = b-1

ans =  math.floor(a * x / b) - a * math.floor(x / b)
print(ans)