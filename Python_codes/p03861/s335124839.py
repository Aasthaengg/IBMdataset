a, b, x = map(int, input().split())

bans = b//x
aans = a//x

if a%x == 0:
    aans -= 1

print(bans - aans)