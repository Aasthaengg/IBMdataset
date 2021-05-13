n = int(input())

max_t = 0
ans = 1

for i in range(2, n + 1, 2):
    t = 0
    j = i
    while j % 2 == 0:
        j //= 2
        t += 1
    else:
        if max_t < t:
            max_t = t
            ans = i
else:
    print(ans)