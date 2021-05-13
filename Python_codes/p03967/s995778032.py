ss = input()

ans = 0
for i, s in enumerate(ss, 1):
    if i % 2: # グーを出す
        if s == 'p':
            ans -= 1
    else: # パーを出す
        if s == 'g':
            ans += 1

print(ans)
