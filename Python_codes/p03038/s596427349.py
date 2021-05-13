import bisect
n,m =list(map(int,input().split()))
a = list(map(int,input().split()))
b = []
for i in range(m):
    c,d = list(map(int,input().split()))
    b.append([d,c])
a.sort()
a.reverse()
b.sort()
b.reverse()
c = []
i = 0
while True:
    if len(c)==n or i == m:
        break
    if b[i][1] >0:
        b[i][1] -=1
        c.append(b[i][0])
    else:
        i += 1
a+=c
a.sort()
a.reverse()
print(sum(a[0:n]))
# print(a)

