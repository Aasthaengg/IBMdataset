N = int(input())

a, b, ba = 0, 0, 0
ret = 0
for _ in range(N):
    s = input()

    ret += s.count('AB')

    cond_a = s[-1] == 'A'
    cond_b = s[0] == 'B'
    if cond_a:
        if cond_b:
            ba += 1
        else:
            a += 1
    else:
        if cond_b:
            b += 1

if ba:
    ret += ba - 1
    if a:
        ret += 1
        a -= 1
    if b:
        ret += 1
        b -= 1
ret += min(a, b)

print(ret)

# ...A
# B...
# B...A
# ... -> 無視
