l = []
min_s = 10
check = 0

for i in range(5):
    a = int(input())
    l.append(a)
    s = int(str(a)[-1])

    if s == 0:
        s = 10
    if s < min_s:
        min_s = s
        check = i

ans = 0
for i in range(len(l)):
    if i == check:
        ans += l[i]
    else:
        if int(str(l[i])[-1]) != 0:
            ans += l[i] + (10-int(str(l[i])[-1]))
        else:
            ans += l[i]

print (ans)
