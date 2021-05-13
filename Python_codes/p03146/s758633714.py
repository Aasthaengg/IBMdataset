s = int(input())
l = []
l.append(s)
i = 1
ans = 2

while True:
    if l[i-1]%2 == 0:
        a = int(0.5*l[i-1])
    else:
        a = 3*l[i-1] +1

    if a in l:
        ans = i + 1
        break
    else:
        i += 1
        l.append(a)
        continue
print(ans)