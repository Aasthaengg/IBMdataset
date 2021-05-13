import collections
n = int(input())
s = input()
ans = 0
for i in range(1,n):
    cnt = 0
    c1 = collections.Counter(s[:i])
    c2 = collections.Counter(s[i:])
    for x in c1.keys():
        if c2[x]: cnt+=1
    ans = max(cnt, ans)
print(ans)