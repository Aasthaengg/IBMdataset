from collections import defaultdict
n, m, k = map(int, input().split())

def is_able(n, m, k):
    res = defaultdict(bool)
    res[0] = True
    for i in range(1, n+1):
        for j in range(1, m+1):
            count = 0
            count += i*j
            count += (n-i)*(m-j)
            res[count] = True
    return res[k]


if is_able(n, m, k):
    print("Yes")
else:
    print("No")