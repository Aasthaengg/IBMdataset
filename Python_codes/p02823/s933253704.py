n, a, b = list(map(int, input().split()))

s = 0
if (a-b) % 2 == 0:
    s = abs(a-b) // 2
else:
    s = min((a+b-1)//2, (2*n - a-b +1)//2)

print(s)
