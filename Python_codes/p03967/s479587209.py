s=list(input())
res = 0
for i in range(len(s)):
    if i%2 == 0:
        if s[i] == 'p':
            res-=1
    else:
        if s[i]=='g':
            res += 1
print(res)