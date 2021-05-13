s=input()
flags=True
for i in range(8):
    if s[:i]=='keyence'[:i] and s[len(s)-7+i:]=='keyence'[i:]:
        print('YES')
        flags=False
        break
if flags:
    print('NO')