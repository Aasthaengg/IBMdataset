n = int(input())

k = -1
for i in range(1, 10 ** 5 + 1):
    if i * (i - 1) == 2 * n:
        k = i
        break

if k == -1:
    print('No')
else:
    ans = [[] for _ in range(k)]
    print('Yes')
    print(k)
    tmp = 1
    for i in range(k):
        for j in range(i+1, k):
            ans[i].append(tmp)
            ans[j].append(tmp)
            tmp += 1

    for i in range(k):
        print(len(ans[i]), *ans[i])

