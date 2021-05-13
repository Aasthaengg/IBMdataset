n = int(input())
l = sorted(list(map(int, input().split())))

if n == 1 and l ==[0, 0]:
    print(1)
    exit()
else:
    a = []
    for i in range(1, n):
        if n % 2 == 1: # odd
            if i < n and i % 2 == 0:
                a += [i] * 2
        else:
            if i < n and i % 2 == 1:
                a += [i] * 2
    else:
        if n % 2 == 1:
            a.insert(0, 0)
    
if l != a:
    print(0)
else:
    print((2 ** (n // 2)) % (10**9 + 7))