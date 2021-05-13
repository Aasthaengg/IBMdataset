S = input()
ans = 0
tmp = ''
pre = ''
for i in S:
    tmp += i
    if pre != tmp:
        pre = tmp
        tmp = ''
        ans += 1
print(ans)