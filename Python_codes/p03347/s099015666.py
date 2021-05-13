a = int(input())
l = []

for i in range(a):
    t = int(input())
    l.append(t)
t =1
res = 0
for i in l[::-1]:
    if i >= t:
        res += i
    elif t - i == 1:
        t = 1
    else:
        l[0] = 1
    t = i
if l[0] ==0 :print(res)
else:print(-1)