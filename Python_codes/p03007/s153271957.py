N=int(input())
a = list(sorted(map(int,input().split())))

result = []
# all +
if a[0] > 0:
    if len(a) == 2:
        print(a[1]-a[0])
        print(a[1], a[0])
        exit()
    result.append((a[0], a[1]))
    t = a[0]-a[1]
    a.pop(0)
    a[0] = t
# all -
elif a[-1] < 0:
    if len(a) == 2:
        print(a[0]-a[1])
        print(a[0], a[1])
        exit()
    result.append((a[-1], a[-2]))
    t = a[-1]-a[-2]
    a.pop(-1)
    a[-1] = t

# print(a)
b = []
for i in range(len(a)-1):
    if a[i] > 0:
        result.append((b[0], a[i]))
        t = b[0]-a[i]
        b[0] = t
    else:
        b.append(a[i])
b.append(a[-1])
# print(b)
while len(b) != 1:
    result.append((b[-1], b[0]))
    b.append(b[-1]-b[0])
    b.pop(0)
    b.pop(-2)
# print(b)

print(b[0])
for r in result:
    print(r[0],r[1])