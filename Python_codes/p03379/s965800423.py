n = int(input())
a = list(map(int, input().split()))

pivots = (sorted(a)[n//2-1], sorted(a)[n//2])
# print(pivots)
for el in a:
    if el <= pivots[0]:
        print(pivots[1])
    else:
        print(pivots[0])