N = int(input())


def basem2(n, ans):
    if n == 0:
        if not ans:
            ans.append(0)
        return ans
    if n > 0:
        p, a, k = 1, 1, 0
        while n > a:
            p *= 4
            a += p
            k += 2
        # print(f"n={n} +{p} bit:{k} => {n-p}")
    else:
        assert n < 0
        p, a, k = -2, -2, 1
        while n < a:
            p *= 4
            a += p
            k += 2
        # print(f"n={n} {p} bit:{k} => {n-p}")
    while len(ans) < k + 1:
        ans.append(0)
    ans[k] = 1
    return basem2(n - p, ans)


print("".join([str(x) for x in reversed(basem2(N, []))]))
