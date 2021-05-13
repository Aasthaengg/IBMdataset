import heapq
n = int(input())
a = [int(input()) for i in range(n)]
maxa = max(a)
ma2 = heapq.nlargest(2, a)[1]
ca = a.count(maxa)
if ca >= 2:
    for i in range(n):
        print(maxa)
else:
    for i in range(n):
        if a[i] == maxa:
            print(ma2)
        else:
            print(maxa)