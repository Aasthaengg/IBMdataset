s = input()
n = len(s)

ans = 'NO'
for i in range(n):
    for j in range(i-1, n):
        string = s[:i] + s[j+1:]
        if string == 'keyence':
            ans = 'YES'
print(ans)