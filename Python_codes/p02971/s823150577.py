n = int(input())
a = list(int(input()) for i in range(n))
b = list(a)
b.sort(reverse = True)
c = b[0]
for i in range(n):
    if a[i] == c:
        print(b[1])
    else:
        print(c)