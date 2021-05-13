import collections
s = input()
c = collections.Counter(s)
n = len(s)
ans = 0
for i in range(len(s)):
    ans += (n-i-c[s[i]])
    c[s[i]]-=1
print(ans+1)