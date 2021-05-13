n,m = map(int, input().split())
mini = 0
maxi = 10**9
for i in range(m):
    l,r = map(int, input().split())
    if mini < l:
        mini = l
    if r < maxi:
        maxi = r
t = maxi -mini + 1
if maxi < mini:
    print(0)
else:
    print(t)