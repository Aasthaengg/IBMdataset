s = input()
ans = []
for i in s:
    cnt = 0
    t = s
    while t.count(i) < len(t):
        cnt += 1
        tmp = ''
        for j in range(len(t)-1):
            if t[j] != i and t[j+1] != i:
                tmp = tmp+t[j]
            else:
                tmp = tmp+i
        t = tmp
    ans.append(cnt)
print(min(ans))
