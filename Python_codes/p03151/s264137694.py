n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

c = 0
tmp = 0
m = []
for i in range(n):
    if a[i] < b[i]:
        c += 1
        tmp -= (b[i]-a[i])
    else:
        m.append(a[i]-b[i])

if tmp == 0:
    print(0)
    exit()

m.sort(reverse=True)
i = 0
while i < len(m):
    tmp += m[i]
    i += 1
    if tmp >= 0:
        print(c+i)
        exit()
        break
print(-1)    