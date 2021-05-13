from collections import defaultdict,Counter

def nck(n, k):
    ret = 1
    for i in range(min(n - k, k)):
        ret *= (n - i)
        ret /= (i + 1)
    return ret


def main():
    n, a, b = map(int, input().split())
    v = list(map(int, input().split()))

    v = sorted(v, reverse=True)
    d = Counter(v)
    value = 0
    t = 0
    for i in range(a):
        value += v[i]
        if i == a - 1:
            t = v[i]
    print(value / a)

    c = 0
    for i in range(n):
        if v[i] == t:
            break
        c += d[v[i]]

    ans = 0
    if d[v[0]] > a:
        for i in range(a, min(b,d[v[0]])+1):
            ans += nck(d[v[0]], i)
        print(int(ans))
    else:
        print(int(nck(d[t], a - c)))


if __name__ == '__main__':
    main()
