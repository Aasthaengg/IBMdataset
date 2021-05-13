from math import factorial


def resolve():
    n, a, b = map(int, input().split())
    v = list(map(int, input().split()))
    v.sort(reverse=True)
    max_ave = sum(v[:a]) / a
    ath = v[a - 1]
    num_ath = v.count(ath)
    large = len([vi for vi in v if vi > ath])
    if v[0] == ath:
        ans = 0
        for i in range(a - large, min(b - large, num_ath) + 1):
            ans += combi(num_ath, i)
    else:
        ans = combi(num_ath, a - large)
    print(max_ave)
    print(ans)


def combi(n, r):
    return factorial(n) // (factorial(n - r) * factorial(r))


if __name__ == "__main__":
    resolve()
