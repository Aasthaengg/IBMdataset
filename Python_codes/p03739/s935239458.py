n = int(input())
a = list(map(int, input().split()))
minnum = float('inf')
for m in range(2):
    ans = 0
    s = [0]*(n+1)
    tmp = a[0] 
    if m == 0:
        if a[0] >= 0:
            ans += a[0]+1
            a[0] = -1 
    else:
        if a[0] <= 0:
            ans += abs(a[0])+1
            a[0] = 1

    for i in range(n):
        s[i+1] = s[i] + a[i]
        if s[i] < 0:
            if s[i+1] != 0 and s[i+1] > 0:
                continue
            else:
                ans += abs(s[i+1])+1
                s[i+1] = 1
        elif s[i] > 0:
            if s[i+1] != 0 and s[i+1] < 0:
                continue
            else:
                ans += abs(s[i+1])+1   
                s[i+1] = -1

    minnum = min(minnum,ans)
    a[0] = tmp

print(minnum) 