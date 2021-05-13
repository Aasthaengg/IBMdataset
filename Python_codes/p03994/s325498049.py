s = input()
k = int(input())
f = lambda x: (ord('a') - ord(x))%26
ans = ''
for c in s:
    if k>=f(c):
        ans += 'a'
        k -= f(c)
    else:
        ans += c
ans = ans[:-1] + chr(ord('a') + (ord(ans[-1])-ord('a')+k)%26)
print(ans)