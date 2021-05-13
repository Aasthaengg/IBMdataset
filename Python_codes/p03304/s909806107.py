a = list(map(int, input().split()))

if a[2] != 0:
    k =float(((2*(a[0]-a[2])*(a[1]-1))/(a[0]**2)))
else:
    k=float((((a[0]-a[2])*(a[1]-1))/(a[0]**2)))

print(k)
