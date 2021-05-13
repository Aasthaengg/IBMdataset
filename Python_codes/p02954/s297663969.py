s = input()
n = len(s)
r = [0]*n
l = [0]*n
for i in range(n-1):
    if s[i] == "R":
        r[i] += 1
        if s[i+1] == "R":
            r[i+2] += r[i]
            r[i] = 0
    if s[-i-1] == "L":
        l[-i-1] += 1
        if s[-i-2] == "L":
            l[-i-3] += l[-i-1]
            l[-i-1] = 0
ans = []
for i in range(n):
    ans.append(r[i]+l[i])
# print(r)
# print(l)
print(*ans)