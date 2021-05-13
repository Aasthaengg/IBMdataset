k, a, b = list(map(int, input().split()))

l = k - (a - 1)
ab = a + (b - a) * (l // 2) + (l % 2) 

print(max(1+k, ab))