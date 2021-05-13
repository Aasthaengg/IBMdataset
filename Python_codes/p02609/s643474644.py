n = int(input())
s = input()[::-1]
cnt = s.count('1')
# 最初にとるあまりは2種類しかない、　一回余りを取ると2 * 10^5以下になる、あとはふつうにできる
# 最初にとるあまりについて->ビット1桁変わるだけ、あまり2種類について最初の状態でのあまりを計算、
# 1桁変わったところはどうするか？->mod二種類で前計算しておいて足す/引く -> もう一回mod
fac0 = [1] * (n + 1)
fac1 = [1] * (n + 1)
for i in range(1, n + 1):
    fac0[i] = fac0[i - 1] * 2 % (cnt + 1)
    if cnt > 1:
        fac1[i] = fac1[i - 1] * 2 % (cnt - 1)


all0 = 0
all1 = 0
for i in range(n):
    if s[i] == '1':
        all0 = (all0 + fac0[i]) % (cnt + 1)
        if cnt > 1:
            all1 = (all1 + fac1[i]) % (cnt - 1)


def pakuri_poppu(c):
    c = (c & 0x5555555555555555) + (c >> 1 & 0x5555555555555555)
    c = (c & 0x3333333333333333) + (c >> 2 & 0x3333333333333333)
    c = (c + (c >> 4)) & 0x0F0F0F0F0F0F0F0F
    return c * 0x0101010101010101 >> 56 & 0x7f


def bon(x):
    p = pakuri_poppu(x)
    res = 1
    while x:
        x %= p
        p = pakuri_poppu(x)
        res += 1
    return res


for i in range(n - 1, -1, -1):
    if s[i] == '0':
        print(bon((all0 + fac0[i]) % (cnt + 1)))
    else:
        if cnt == 1:
            print(0)
            continue
        print(bon((all1 - fac1[i]) % (cnt - 1)))
