N = int(input())
cnt = 0
for n in range(1, N + 1, 2):
    route_n = int(n ** (1 / 2))
    by = [] 
    for i in range(1, route_n + 1, 2):
        if n % i == 0:
            by.append(i)
            a = n // i
            if a != i:
                by.append(a)
    if len(by) == 8:
        cnt += 1

print(cnt)