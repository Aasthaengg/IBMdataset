n = int(input())
a = list(map(int, input().split()))
s = [[0]*20]
for i in a:
    tmp = []
    for j in range(20):
        tmp.append((i>>j&1)+s[-1][j])
    s.append(tmp)
l = 0
r = 0
ans = 0
while l < n:
    for j in range(20):
        if s[r+1][j]-s[l][j]>1:
            ans += r-l
            l += 1
            break
    else:
        if r < n-1:
            r += 1
        else:
            ans += n-l
            l += 1
print(ans)
