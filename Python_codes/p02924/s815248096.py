#!/use/bin/env python3

a = input()

b = int(a)

ans = 0

if b != 2:
    if b % 2 == 1:
        ans = b * ((b - 1) // 2)
    else:
        ans = b * ((b - 1) // 2) + (b // 2)
else:
    ans = 1

print(ans)