n,h = map(int,input().split())
a = [0]*n
b = [0]*n
for i in range(n):
    a[i], b[i] = map(int,input().split())
a = sorted(a, reverse=True)
b = sorted(b, reverse=True)
c = 0
j = 0
while j<n:
    if b[j] > a[0]:
        c += b[j]
    else:
        break
    j += 1
    if c >= h:
        break

if c < h:
    j += -(-(h-c)//a[0])
print(j)