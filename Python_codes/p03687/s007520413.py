s = input()
ans = float('inf')
for x in s:
    cnt = 0
    temp = s
    while len(set(temp))!=1:
        t = ''
        for i in range(len(temp)-1):
            if temp[i+1]==x:
                t += temp[i+1]
            else:
                t += temp[i]
        temp = t
        cnt += 1
    ans = min(ans,cnt)
print(ans)