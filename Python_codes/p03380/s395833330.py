n = int(input())
a = list(map(int, input().split()))

a.sort()
left = a.pop()
yoi = left/2
for i in range(n-1):
    if a[i] >= yoi:
        a[i] = (abs(a[i]-yoi), 1)
    else:
        a[i] = (abs(a[i]-yoi), -1)
a.sort()
right = abs(int(a[0][0]+a[0][1]*yoi))
print(left, right)