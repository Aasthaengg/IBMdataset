s = input()

n = len(s)
ok = False
ans = 9
if n == 1:
    print(s)
    exit()

for i in range(n-1):
    if ok:
        ans += 9
        continue
    if s[i+1] == '9':
        ans += ord(s[i]) - ord('0')
        continue
    x = ord(s[i]) - ord('0')
    ans += x-1
    ok = True

print(ans)
