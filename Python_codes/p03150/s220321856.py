s = input()
tgt = 'keyence'
ans = 'NO'
for i in range(8):
    if s[:i] == tgt[:i] and s[len(s)-(7-i):] == tgt[i:]:
        ans = 'YES'
        break
print(ans)