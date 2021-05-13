
from collections import Counter, defaultdict
def resolve():
    H, W = map(int, input().split())
    S = Counter()
    for _ in range(H):
        S.update(list(input()))

    dd = defaultdict(int)
    for k, v in S.items():
        q, r = divmod(v, 4)
        dd[4] += q
        qq, rr = divmod(r, 2)
        dd[2] += qq
        dd[1] += rr

    ans = "Yes"

    if H % 2 == 0 and W % 2 == 0:
        if dd[2] != 0 or dd[1] != 0:
            ans = "No"
    elif H % 2 == 0:
        if dd[1] != 0 or dd[2] > H // 2:
            ans = "No"
    elif W % 2 == 0:
        if dd[1] != 0 or dd[2] > W // 2:
            ans = "No"
    else:
        if dd[1] != 1:
            ans = "No"
        else:
            if dd[2] > H // 2 + W // 2:
                ans = "No"

    print(ans)


if __name__ == "__main__":
    resolve()
