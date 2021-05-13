n, k = map(int, input().split())
r,s,p = map(int, input().split())
t = list(input())

ans = 0

for i in range(n):
    valian = t[i]
    if valian == 'r':
        ans += p
    elif valian == 's':
        ans += r
    else:
        ans += s
        
for i in range(k):
    check = ''
    for j in range(i, n, k):
        if check == '':
            check = t[j]
            continue
        
        if check == t[j]:
            if t[j] == 'r':
                ans -= p
            elif t[j] == 's':
                ans -= r
            else:
                ans -= s
            check = ''
        else:
            check = t[j]
        
print(ans)