n = int(input())
s = input()
t = set(s)
ans = 0

for i in range(1,n):
    count = 0
    s1 = s[:i]
    s2 = s[i:]
    for i in t:
        if s1.count(i) > 0 and s2.count(i) > 0:
            count += 1
            
    if ans < count:
        ans = count
print(ans)