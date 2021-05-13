def make_divisors(n):
    ret = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            ret.append(d)
            if d != n // d:
                ret.append(n // d)
        d += 1
    return ret

# n = int(input())
def test(n):
    ret = 0
    for i in range(1, n + 1):
        if n // i == n % i:
            ret += i
    return ret


def main(n):
    d = make_divisors(n)
    # print("d =", d)
    ans = 0
    for i in d:
        m = i - 1
        if 1 <= n // (m + 1) < m:
            ans += m
    return ans
    # print(ans)

n = int(input())
print(main(n))

# for i in range(1, 1000):
#     ans_main = main(i)
#     ans_test = test(i)
#     if ans_main != ans_test:
#         print(i)        
#         print("ans_main =", ans_main)
#         print("ans_test =", ans_test)