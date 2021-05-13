n = int(input())

k = (1 + (1 + 8 * n)** 0.5) * 0.5
if k.is_integer():
    k = int(k)
    print('Yes')
    print(k)
    num,ans = 1,[[] for _ in range(k)]
    for i in range(k):
        for j in range(i + 1, k):
            ans[i].append(num)
            ans[j].append(num)
            num += 1
        print(k - 1, *ans[i])
else:
    print('No')
