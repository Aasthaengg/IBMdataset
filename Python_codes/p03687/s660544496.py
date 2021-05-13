s = input()
ss = set(s)
# print(ss)
ans = float('inf')
for si in ss:
    cnt = 0
    copy_s = list(s)
    # print(copy_s)
    while len(set(copy_s)) != 1:
        # copy_s.pop()
        cnt += 1
        for i in range(len(copy_s)-1):
            if copy_s[i+1] == si:
                copy_s[i] = si
        copy_s.pop()
    ans = min(ans, cnt)

print(ans)