from collections import Counter


def main():
    H, W = map(int, input().split())
    a = ""
    for _ in range(H):
        a += input()
    c = Counter(a)
    cnt = [0] * 4
    for _, v in c.items():
        cnt[v % 4] += 1

    if cnt[3] > 0:
        cnt[1] += 1
        cnt[2] += 1
        cnt[3] -= 1

    if H % 2 == 1 and W % 2 == 1:
        if cnt[3]:
            return "No"
        if cnt[1] != 1:
            return "No"
        if cnt[2] > (H - 1) // 2 + (W - 1) // 2:
            return "No"
        return "Yes"
    elif H % 2 == 0 and W % 2 == 0:
        if cnt[1] or cnt[2] or cnt[3]:
            return "No"
        else:
            return "Yes"
    else:
        # Hが奇数，Wが偶数
        if W % 2 == 1:
            tmp = W
            W = H
            H = tmp
        if cnt[1] or cnt[3]:
            return "No"
        if cnt[2] > W // 2:
            return "No"
        return "Yes"


print(main())
