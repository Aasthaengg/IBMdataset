import copy

s = input()
n = len(s)

ans = 10**10

if len(set(list(s))) == 1:
    print(0)
    exit()

for i in range(26):
    t = chr(i + ord('a'))
    tmp = 0
    li = [False] * n
    for j in range(n):
        if s[j] == t:
            li[j] = True
    while True:
        li_tmp = [False] * (n - tmp - 1)
        for j in range(n-tmp):
            if li[j]:
                if j > 0:
                    li_tmp[j-1] = True
                if j < n-tmp-1:
                    li_tmp[j] = True
        tmp += 1
        if all(li_tmp):
            ans = min(ans, tmp)
            break
        else:
            li = copy.copy(li_tmp)

print(ans)
