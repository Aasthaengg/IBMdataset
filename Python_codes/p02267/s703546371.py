n = int(input())
s = input().split()
for i, x in enumerate(s):
    s[i] = int(x)
q = int(input())
t = input().split()
for i, x in enumerate(t):
    t[i] = int(x)

c = 0
for x_t in t:
    for x_s in s:
        if x_t == x_s:
            c += 1
            break

print(c)
