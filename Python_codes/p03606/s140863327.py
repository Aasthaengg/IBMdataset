lr = []
l = []
r = []
n = int(input())
c = 0
for i in range(0,n):
    lr = input().split()
    l.append(int(lr[0]))
    r.append(int(lr[1]))

for i in range(0,n):
    if l[i] == r[i]:
        c += 1
    else:
        c += (1 + r[i] - l[i])

print(c)
