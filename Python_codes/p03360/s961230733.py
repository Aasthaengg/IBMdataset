a, b, c = (int(x) for x in input().split())
k = int(input())
m = max(a, b, c)
print(a + b + c + m * 2**k - m)
