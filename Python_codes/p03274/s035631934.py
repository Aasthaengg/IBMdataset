n,k = map(int,input().split())
a = list(map(int,input().split()))
b = []
c = [0]
for i in range(n):
    if a[i] < 0:
        b.append(abs(a[i]))
    elif a[i] > 0:
        c.append(a[i])
    else:
        k-=1
if k == 0:
    print(0)
    exit()
b.append(0)
b = b[::-1]
if len(b) == 1:
    print(c[k])
    exit()
if len(c) == 1:
    print(b[k])
    exit()
ans = 10 ** 18
for i in range(len(b)):
    if k - i >= len(c):
        continue
    if i == k:
        break
    #print(2*b[i]+c[k-i],b[i]+2*c[k-i])
    ans = min(ans,min(2*b[i]+c[k-i],b[i]+2*c[k-i]))
print(ans)