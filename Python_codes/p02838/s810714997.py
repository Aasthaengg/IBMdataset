def str2bitstr(chs):
    val = int(chs)
    tmp = bin(val)[2:]
    tmp2 = '0' * (60 - len(tmp))
    return tmp2 + tmp


n = int(input())
a = list(map(str2bitstr, input().split()))

cnts = [0] * 60

for item in a:
    for i, ch in enumerate(item):
        if ch == '1':
            cnts[i] += 1

ret = 0
now = 1

for i in range(1, 61):
    kumi = cnts[-i] * (n - cnts[-i]) % (10 ** 9 + 7)
    ret += kumi * now % (10 ** 9 + 7)
    now *= 2 % (10 ** 9 + 7)
    ret = ret % (10 ** 9 + 7)

print(ret % (10 ** 9 + 7))
