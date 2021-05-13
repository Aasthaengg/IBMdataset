def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    import collections
    counter = collections.Counter(A)
    #print(counter)
    Q = int(input())
    BC = [list(map(int, input().split())) for _ in range(Q)]
    ans = sum(A)
    for b, c in BC:
        if b in counter:
            ans -= b*counter[b]
            ans += c*counter[b]
            if c not in counter:
                counter[c] = 0
            counter[c] += counter[b]
        counter[b] = 0
        #print(counter)
        print(ans)


if '__main__' == __name__:
    resolve()
