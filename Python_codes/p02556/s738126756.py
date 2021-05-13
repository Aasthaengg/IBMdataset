n = int(input())
xy = [list(map(int,input().split()))for _ in range(n)]

iti = -float("inf")
ni = -float("inf")
san = -float("inf")
yon = -float("inf")
for x,y in xy:
    iti = max(iti,x+y)
    ni = max(ni,x-y)
    san = max(san,-x+y)
    yon = max(yon,-x-y)

print(max(iti+yon,ni+san))