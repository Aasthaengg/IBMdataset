n = int(input())
a = list(map(int, input().split()))

sm = a[0]


def f(sm):
    ret = 0
    for e in a[1:]:
        if sm * (sm + e) < 0:
            sm += e
            continue

        else:
            if sm > 0:
                a_mx = -sm - 1
                ret += e - a_mx
                sm += a_mx
            else:
                a_mn = -sm + 1
                ret += a_mn - e
                sm += a_mn

    return ret


if sm > 0:
    ans = min(f(sm), f(-1) + sm + 1)
elif sm < 0:
    ans = min(f(sm), f(1) - sm + 1)
else:
    ans = min(f(1), f(-1)) + 1

print(ans)
