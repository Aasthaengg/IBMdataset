k = int(input())
a = list(map(int, input().split()))
if a[-1] != 2:
    print(-1)
    quit()
l, r = 2, 3
for i in range(k-2, -1, -1):
    s = ((l-1)//a[i]+1) * a[i]
    if s > r:
        print(-1)
        quit()
    t = ((r-1)//a[i]+1) * a[i]
    t = t-1 if t > r else t+a[i]-1
    l, r = s, t
print(l, r)