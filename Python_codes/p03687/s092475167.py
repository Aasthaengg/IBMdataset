l = list(input())
ans = 10000000
for let in range(26):
    cur = chr(let+97)
    temp = l[:]
    cnt = 0
    while len(set(temp)) > 1:
        for i in range(len(temp)-1):
            if temp[i] == cur or temp[i+1] == cur:
                temp[i] = cur
            else:
                temp[i] = l[i]
        temp.pop()
        cnt += 1
    ans = min(ans, cnt)
    # print(temp)
print(ans)