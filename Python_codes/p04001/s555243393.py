s = input()
n= len(s)
ans = 0
for i in range(0, 2**(n-1)):
    tmp = int(s[0])
    for j in range(n-1):
        if (i >> j) & 1:
            ans += tmp
            tmp = int(s[j+1])
        else:
            tmp *= 10
            tmp += int(s[j+1])
    ans += tmp
print(ans)