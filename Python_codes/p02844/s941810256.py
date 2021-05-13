n = int(input())
s = input()

cnt = 0
for i in range(1000):
    pin = '%03d' % i
    try:
        i0 = s.index(pin[0])
        i1 = i0 + 1 + s[i0+1:].index(pin[1])
        i2 = i1 + 1 + s[i1+1:].index(pin[2])
        cnt += 1
    except ValueError:
        pass

print(cnt)