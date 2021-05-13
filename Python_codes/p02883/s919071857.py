n,k = map(int,input().split())
a = list(map(int,input().split()))
f = list(map(int,input().split()))

a.sort()
f.sort(reverse=True)

r = 10**12
l = -1

def test(x):
    point = 0
    for i in range(n):
        point += max(0,a[i]-x//f[i])
    return point <= k

def nibutan(low,hi):
    while True:
        ave = (low+hi)//2
        if test(ave):
            hi = ave
        else:
            low = ave
        if hi-low == 1:
            break
    return hi

print(nibutan(l,r))