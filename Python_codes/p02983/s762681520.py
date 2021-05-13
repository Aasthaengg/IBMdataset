L, R = map(int, input().split())

# 前提として、LとRの差が2019より小さいとき

# modを比較し、LよりRの方が大きい時は2019の倍数を通り越していない
# modを比較し、LよりRの方が小さい時は2019の倍数を通り越している

deff = R - L
if (deff < 2019):
    min_num = 10**9 + 7
    for i in range(L, R):
        for j in range(i + 1, R + 1):
            min_num = min(min_num, (i * j) % 2019)
    print(min_num)
else:
    print(0)
