# TLE 1/13 corner0
x = input()
while 'ST' in x:
    x = x.replace('ST', '')
    # 以下の4行を加えて AC  'SSS..STTTTT..T' みたいなやつを検出
    n = len(x) // 2
    if ('T' not in x[:n]) and ('S' not in x[n:]):
        x = ''
        break
print(len(x))
