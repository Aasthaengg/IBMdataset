s = str(input())
t = str(input())

n = len(s)
m = len(t)
if m > n:
    print('UNRESTORABLE')
    exit()

ans = []
for i in range(n-m+1):
    flag = True
    for j in range(m):
        if s[i+j] != t[j]:
            if s[i+j] != '?':
                flag = False
    if flag:
        p = s[:i]
        q = s[i+m:]
        temp = p.replace('?', 'a')+t+q.replace('?', 'a')
        ans.append(temp)

ans.sort()
if ans:
    print(ans[0])
else:
    print('UNRESTORABLE')
