def prime(n):
    p = []
    flag = [True] * (n - 1)
    for i in range(n - 1):
        if flag[i] == True:
            p.append(i + 2)
            num = i
            while num <= n - 2:
                flag[num] = False
                num += i + 2
    return set(p)

p1 = prime(10 ** 5)
p2 = [0]
for i in range(10 ** 5):
    if i % 2 == 1:
        p2.append(p2[-1])
        continue
    else:
        if i + 1 in p1 and (i + 2) // 2 in p1:
            p2.append(p2[-1] + 1)
        else:
            p2.append(p2[-1])
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(p2[r] - p2[l -1])