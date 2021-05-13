N = int(input())
K = (((8 * N + 1) ** (1/2) + 1) / 2)

def recursive(k):
    if k == 2:
        return [[1], [1]]
    else:
        before = recursive(k - 1)
        r = [_ for _ in range(1 + (k - 2) * (k - 1) // 2, 1 + k * (k - 1) // 2)]
        return ([before[_] + [r[_]] for _  in range(len(r))] + [r])

if K.is_integer():
    K = int(K)
    print('Yes')
    print(K)
    [print(K - 1, ' '.join(map(str, ary))) for ary in recursive(K)]
else:
    print('No')