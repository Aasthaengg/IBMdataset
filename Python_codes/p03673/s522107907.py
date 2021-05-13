n = int(input())
a = list(map(int, input().split()))
ol = []
el = []

for i in range(n):
    if i%2 == 0:
        ol.append(a[i])
    else:
        el.append(a[i])

if n%2 == 0:
    for i in el[::-1]:
        print(i, end = " ")
    for i in ol:
        print(i, end = " ")
else:
    for i in ol[::-1]:
        print(i, end = " ")
    for i in el:
        print(i, end = " ")