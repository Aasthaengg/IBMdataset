s = input()
ans = 0
for i in range(1<<(len(s)-1)):
    tmp = s[0]
    for j in range(len(s)-1):
        if i&(1<<j):
            tmp += '+'
        tmp += s[j+1]
    ans += eval(tmp)
print(ans)