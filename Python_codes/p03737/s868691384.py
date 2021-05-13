S = list(map(str,input().split()))
ans = ''
for s in S:
    ans += chr(ord(s[0])-32)
print(ans)