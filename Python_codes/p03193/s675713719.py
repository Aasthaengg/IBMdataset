n,h,w = map(int,input().split())
a = []
b = []
count = 0
for i in range(n):
    a1,b1 = map(int,input().split())
    a.append(a1)
    b.append(b1)
for i in range(n):
    if a[i] >= h and b[i] >= w:
        count += 1
print(count)