n = int(input())
lens = list(map(int, input().split()))
lens.sort(reverse=True)

res = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        if lens[i] == lens[j]:
            continue
        for k in range(j + 1, n):
            if lens[i] == lens[k] or lens[j] == lens[k]:
                continue
            if lens[i] < lens[j] + lens[k]:
                res += 1

print(res)
