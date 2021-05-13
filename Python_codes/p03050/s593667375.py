n = int(input())
c = 1
li = []
while True:
    k = n-c
    if k//c <= c:
        break
    if k % c == 0:
        li.append(k//c)
    c += 1
print(sum(li))