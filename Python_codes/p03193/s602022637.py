n,h,w = map(int,input().split())
a = []
b = []
for i in range(n):
    tmp1,tmp2 = map(int,input().split())
    a.append(tmp1)
    b.append(tmp2)
counter = 0
for i in range(n):
    if a[i] >= h and b[i] >= w:
        counter +=1
print(counter)