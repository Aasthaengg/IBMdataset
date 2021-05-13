n = int(input())
a = list(map(int,input().split()))
t = [0] * 8
p = 0

for i in range(n):
    if a[i] < 3200:
        t[a[i] // 400] = 1
    else:
        p += 1

x = t.count(1)
amax = p+x
if x == 0:
    amin = 1
else:
    amin = x
print(amin,amax)