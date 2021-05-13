s = input()
se = s.replace('x','')
if se != se[::-1]:
    print(-1)
else:
    xc = []
    now = 0
    for i in s:
        if i == 'x':
            now += 1
        else:
            xc.append(now)
            now = 0
    xc.append(now)
    ans = 0
    for i in range(len(xc)//2):
        ans += abs(xc[i]-xc[-i-1])
    print(ans)
