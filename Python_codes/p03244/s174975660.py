from collections import Counter
def main():
    N = int(input())
    V = list(map(int, input().split()))
    c0 = Counter(V[::2])
    c1 = Counter(V[1::2])
    cc0 = sorted([(0, 0)] + [(v, k) for k, v in c0.items()], reverse=True)
    cc1 = sorted([(0, 0)] + [(v, k) for k, v in c1.items()], reverse=True)
    m0, v0 = cc0[0]
    m1, v1 = cc1[0]
    if v0 != v1:
        return N - m0 - m1
    return min(N - m0 - cc1[1][0], N - m1 - cc0[1][0])
print(main())
