n = int(input())
a = [int(input()) for _ in range(n)]
maxa = max(a)
# print(maxa)
if a.count(maxa) == 1:
    b = sorted(a, reverse=True)

    maxa2 = b[1]
    for i in range(n):
        if a[i] == maxa:
            print(maxa2)
        else:
            print(maxa)

else:
    for i in range(n):
        print(maxa)
