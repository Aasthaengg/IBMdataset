s = input()
t = input()

a = list(s)
b = list(t)

answer = False

for i in range(len(a)):
    if a == b:
        answer = True
        break
    else:
        c = []
        p = a[len(a)-1]
        c.append(p)
        for j in range(len(a)-1):
            c.append(a[j])
        for h in range(len(a)):
            a[h] = c[h]

if answer:
    print('Yes')
else:
    print('No')