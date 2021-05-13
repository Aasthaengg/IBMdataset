n = int(input())
a = b = 0
for _ in range(n):
    s1, s2 = [i for i in input().split()]
    if s1 == s2:
        a += 1
        b += 1
    elif s1 > s2: a += 3
    else: b += 3
print(a,b)