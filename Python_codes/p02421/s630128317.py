n=int(input())
s=[0,0]
for i in range(n):
    t, h = input().strip().split()
    if t>h:
        s[0] += 3
    elif t<h:
        s[1] += 3
    else:
        s[0] += 1
        s[1] += 1
print(*s)