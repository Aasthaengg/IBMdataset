# 入力
N = int(input(''))

# もしNが999以下ならABC、1000以上ならABD
if N <= 999:
    print('ABC')
elif N >= 1000:
    print('ABD')
else:
    print('Error')
