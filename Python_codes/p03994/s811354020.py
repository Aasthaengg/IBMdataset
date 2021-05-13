s = input()
k = int(input())
ans = ''
for i,v in enumerate(s):
    if (ord('a') - ord(v))%26 <= k:
        k -= (ord('a') - ord(v))%26
        ans += 'a'
    else:
        ans += v
k %= 26
last = chr(ord('a')+(ord(ans[-1])-ord('a')+k)%26)

print(ans[:-1]+last)

