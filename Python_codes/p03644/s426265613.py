N = int(input())
c = 0
ans = 1
for i in range(1, N + 1):
    n = i
    for t in range(N + 1):
        if n % 2 != 0:
            if c < t:
                c = t
                ans = i
            break
        n //= 2
print(ans)
