from collections import Counter
N = int(input())
A = list(map(int, input().split()))

c = Counter(A)
n = len(c)
if ((n == 1 and c[0] > 0)
        or (n == 2 and c[0] == N//3)):
    print('Yes')
elif n == 3:
    x, y, z = c.keys()
    if x ^ y ^ z == 0 and all(n == N // 3 for n in c.values()):
        print('Yes')
    else:
        print('No')
else:
    print('No')
