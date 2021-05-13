n,k = map(int,input().split())
s = input()
l = x = ans = 0
for r in range(n):
    if s[r] == '0' :
        if r == 0 or s[r-1] == '1':
            x += 1
    if x > k:
        while s[l] == '1':
            l += 1
        while s[l] == '0':
            l += 1
        x -= 1
    ans = max(ans,r-l+1)
print(ans)