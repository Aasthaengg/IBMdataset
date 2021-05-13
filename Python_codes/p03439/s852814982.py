from math import ceil
N = int(input())
cnt = 1
print(0)
S = input()
if S == 'Vacant':
    exit()
d = {'Male': 1, 'Female': 0}
sex = [-1,-1]
sex[0] = d[S]
l = 0
r = N-1
print(r)
S = input()
if S == 'Vacant':
    exit()
sex[1] = d[S]
while True:
    mid = (l+r)//2
    if mid % 2 !=0 and r-l > 2:
        mid -= 1
    print(mid)
    S = input()
    if S == 'Vacant':
        exit()
    if d[S] == sex[0]:
        l = mid
    else:
        r = mid