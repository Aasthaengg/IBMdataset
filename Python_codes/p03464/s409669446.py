from math import ceil
K = int(input())
A = list(map(int, input().split()))
A.reverse()
if A[0] != 2:
    print(-1)
    exit()
mi = 2
mx = 3
for a in A[1:]:
    if ceil(mi/a) > mx//a:
        print(-1)
        exit()
    mi = ceil(mi/a)*a
    mx = mx//a*a
    mx = mx + a - 1
print(mi, mx)