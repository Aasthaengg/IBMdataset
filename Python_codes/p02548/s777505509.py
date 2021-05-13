def func(x):
    ans = 0
    for a in range(1, n):
        for b in range(1, n):
            c = n - a * b
            if c <= 0:
                break
            ans += 1
    return ans

n = int(input())
print(func(n))