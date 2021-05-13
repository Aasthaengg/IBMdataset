# https://atcoder.jp/contests/abc105/tasks/abc105_c

n = int(input())

if n == 0:
    print('0')
else:
    # Sの先頭は必ず1、つまり最大桁は1と決まっている。
    s = ''
    n *= -1
    while n:
        t = n % -2
        if t < 0:
            t *= -1
        s = str(t) + s
        n //= -2
    print(s)