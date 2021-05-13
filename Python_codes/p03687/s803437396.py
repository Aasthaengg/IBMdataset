s = input()
a = [[-1] for i in range(26)]

for i in range(len(s)):
    a[ord(s[i])-ord('a')].append(i)

for i in range(26):
    a[i].append(len(s))

ans = float('inf')
for i in range(26):
    ma = 0
    for j in range(1,len(a[i])):
        dis = a[i][j]-a[i][j-1]-1
        ma = max(dis,ma)
    ans = min(ma,ans)

print(ans)
