n,h = map(int,input().split())
a = [0] * n
b = [0] * n
for i in range(n):
    a[i],b[i] = map(int,input().split())

ama = max(a)
b.sort(reverse=True)
c = 0
i = 0
while(h > 0):
    if(i >= n):break
    if(b[i] > ama):
        c += 1
        h -= b[i]
        i += 1
    else:
        break
h = max(0,h)
c += h // ama
if(h % ama != 0):c += 1
print(c)