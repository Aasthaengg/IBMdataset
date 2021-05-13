n, m, x = map(int, input().split())
a = list(map(int, input().split()))

s1 = 0
s2 = 0
for num in a:
    if num < x:
        s1 += 1
    elif num > x:
        s2 += 1
print(min(s1, s2))
