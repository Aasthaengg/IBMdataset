n = int(input())
s = input()
ans = 0

for i in range(1,n):
    cnt = 0
    x = s[:i]
    y = s[i:]

    x = set(x)
    y = set(y)
    for j in x:
        if j in y: cnt+= 1
    ans = max(ans,cnt)
print(ans)