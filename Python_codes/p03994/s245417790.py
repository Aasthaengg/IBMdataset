s = str(input())
k = int(input())

n = len(s)

l = [0]*n
for i in range(n):
    l[i] = ord('z') -ord(s[i]) + 1
    l[i] %= 26
#print(l)

ans = list(s)
i = 0
while k > 0:
    if i > n-1:
        break
    if l[i] <= k:
        ans[i] = 'a'
        k -= l[i]
    i += 1
k %= 26
if k > 0:
    ans[-1] = chr((k + ord(ans[-1])-ord('a'))%26+97)
#print(ans)
print(''.join(ans))
