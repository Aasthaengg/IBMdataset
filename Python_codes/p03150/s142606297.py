s = input()

k = 'keyence'

ok = False
for i in range(8):
    if s[0:i] == k[0:i] and s[-7+i:] == k[-7+i:]:
        ok = True
        break

print('YES' if ok else 'NO')
