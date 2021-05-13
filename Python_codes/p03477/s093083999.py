a = list(map(int, input().split()))
l = (a[0] + a[1])
r = (a[2] + a[3])
if l > r:
    print('Left')
elif l == r:
    print('Balanced')
else:
    print('Right')