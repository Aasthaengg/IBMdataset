a, b, c = sorted(map(int, input().split()), reverse=True)

parity = (a + b + c) % 2 # 総和の偶奇
m3 = (a*3) % 2 # 最大値×3の偶奇

if parity == m3:
    x = a
else:
    x = a + 1

print((x*3 - (a+b+c)) // 2)