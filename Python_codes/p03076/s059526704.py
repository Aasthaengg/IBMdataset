li = []
for i in range(5):
    li.append(int(input()))
mi = 10
for i in range(5):
    a = li[i]%10
    if mi > a and a != 0:
        mi = a
        t = i
if mi != 10:
    a = li[t]
    li.remove(a)
    for i in range(4):
        if li[i] % 10 != 0:
          li[i] += (10 - li[i] % 10)
    print(sum(li) + a)
else:
    print(sum(li))