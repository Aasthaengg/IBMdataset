import collections
n = int(input())
s = [input() for _ in range(n)]
# s.append('')
m = int(input())
t = [input() for _ in range(m)]
# t.append('')
sc = collections.Counter(s)
tc = collections.Counter(t)
# print(sc, tc)
ans = 0
for string, times in sc.items():
    if string in tc.keys():
        ans = max(ans, times - tc[string])
    else:
        ans = max(ans, times)
        
        
print(ans)
