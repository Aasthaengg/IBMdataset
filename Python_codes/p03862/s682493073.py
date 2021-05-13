N, x = map(int, input().split())
alist = list(map(int, input().split()))
gokei = 0
if alist[0] > x:
    reduceBox = alist[0] - x
    gokei += reduceBox
    alist[0] = alist[0] - (reduceBox)
 
for i in range(N - 1):
    eat = alist[i] + alist[i+1] - x
    if eat > 0:
        gokei += eat
        alist[i+1] = alist[i+1] - eat
print(gokei)