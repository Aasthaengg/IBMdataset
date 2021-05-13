n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = str(input())

ans = 0
temp = [0]*n
for i in range(n):
    if i <= k-1:
        if t[i] == 'r':
            ans += p
        elif t[i] == 's':
            ans += r
        else:
            ans += s
    else:
        if t[i-k] == t[i]:
            if temp[i-k] == 0:
                temp[i] = -1
            else:
                if t[i] == 'r':
                    ans += p
                elif t[i] == 's':
                    ans += r
                else:
                    ans += s
                temp[i] = 0
        else:
            if t[i] == 'r':
                ans += p
            elif t[i] == 's':
                ans += r
            else:
                ans += s
            temp[i] = 0

    #print(i, ans)
print(ans)
