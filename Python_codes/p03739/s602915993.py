N = int(input())
A = list(map(int,input().split()))

ans1 = c = 0
for i,a in enumerate(A):
    if i%2==0:
        if c+a > 0:
            c += a
        else:
            d = 1-(c+a)
            ans1 += d
            c = 1
    else:
        if c+a < 0:
            c += a
        else:
            d = c+a+1
            ans1 += d
            c = -1

ans2 = c = 0
for i,a in enumerate(A):
    if i%2:
        if c+a > 0:
            c += a
        else:
            d = 1-(c+a)
            ans2 += d
            c = 1
    else:
        if c+a < 0:
            c += a
        else:
            d = c+a+1
            ans2 += d
            c = -1

print(min(ans1, ans2))