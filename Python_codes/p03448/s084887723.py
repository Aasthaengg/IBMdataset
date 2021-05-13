# L 500円　M 100円　S 50円 N 合計
L = int(input())  # 10
M = int(input())  # 2
S = int(input())  # 1
N = int(input())
count = 0


def sum(l=0, m=0, s=0):
    return 500 * l + 100 * m + 50 * s


for l in range(L + 1):
    if N == sum(l):
        count += 1
        break
    else:
        for m in range(M + 1):
            if N == sum(l, m):
                count += 1
                break
            else:
                for s in range(S + 1):
                    if N == sum(l, m, s):
                        count += 1
                        break
print(count)
