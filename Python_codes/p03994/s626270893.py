alp1 = list('abcdefghijklmnopqrstuvwxyz'[::-1])
num = [i for i in range(1,26)]
alp = {}
for a,n in zip(alp1,num):
    alp[a] = n
s = input()
K = int(input())
ans =''
now = 0
while True:
    if s[now] == 'a':
        ans += 'a'
    elif K >= alp[s[now]]:
        K -= alp[s[now]]
        ans += 'a'
    else:
        ans += s[now]
    now += 1
    if now == len(s):
        break
if K:
    alp1 = alp1[::-1]
    last = ans[-1]
    ans = ans[:-1]
    ind = alp1.index(last)
    ind = (ind+K)%26
    ans += alp1[ind]
    print(ans)
else:
    print(ans)