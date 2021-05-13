from sys import stdin

MOD = 2019
L, R = [int(x) for x in stdin.readline().split(' ')]

# 2019最大と最小の間が2019以上だったらピッタリ2019で割り切れる値が作れる
if R - L >= 2019:
    print(0)
    exit()

min_val = 2 * 10**9

for i in range(L, R):
    for x in range(i+1, R+1):
        a = (i % MOD * x % MOD) % MOD

        if a == 0:
            print(0)
            exit()

        if a < min_val:
            min_val = a

print(min_val)
