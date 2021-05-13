# A - Colorful Transceivers

# A,B,Cの3人が、直接的あるいは間接的に会話できるなら Yes を、
# そうでないなら No を返す

a, b, c, d = map(int, input().split())

ac = abs(a - c)
ab = abs(a - b)
bc = abs(b - c)

if ac <= d \
or (ab <= d and bc <= d):
    print('Yes')
else:
    print('No')
