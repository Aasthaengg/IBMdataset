N = int(input())
exist = False
num = None
for K in range(1, N+1):
    if K * (K + 1) // 2 == N:
        exist = True
        num = K
        break

if not exist:
    print("No")
else:
    print("Yes")
    print(num + 1)
    res = [[] for _ in range(num + 1)]
    tot = 1
    for k in range(num, 0, -1):
        for i in range(k):
            res[num - k].append(tot + i)
            res[num - k + i + 1].append(tot + i)
        tot += k

    for i in range(num + 1):
        ans = []
        ans.append(len(res[i]))
        ans += res[i]
        print(" ".join(map(str, ans)))

