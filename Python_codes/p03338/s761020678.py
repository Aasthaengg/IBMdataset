n = int(input())
s = list(input())
p = 0

for i in range(1,n):
    a = list(s[0:i])
    a = list(set(a))
    b = list(s[i:])
    t = 0
    for j in range(len(a)):
        if a[j] in b:
            t += 1
    p = max(t,p)

print(p)