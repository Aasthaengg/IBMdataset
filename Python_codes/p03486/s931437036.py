s = list(input())
t = list(input())
n, m = len(s), len(t)
s.sort()
t.sort(reverse = True)
if n < m:
    jud = True
else:
    jud = False
for i in range(min(n, m)):
    if s[i] > t[i]:
        jud = False
        break
    elif s[i] < t[i]:
        jud = True
        break
if jud:
    print("Yes")
else:
    print("No")