n = int(input())

if n % 2 == 1:
    ans = []
    count = 0

    for i in range(1, n):
        ans.append((i, n))
        count += 1

    for i in reversed(range(1, n)):
        for j in range(1, i):
            if i + j == n:
                continue
            ans.append((j, i))
            count += 1

    print(count)
    for a, b in ans:
        print(a, b)
else:
    ans = []
    count = 0

    for i in reversed(range(1, n+1)):
        for j in range(1, i):
            if i + j == n+1:
                continue
            ans.append((j, i))
            count += 1

    print(count)
    for a, b in ans:
        print(a, b)
