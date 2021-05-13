a = list(map(int, input().split()))
a.sort()

print(int(a[0]*a[1]*(a[2] - a[2]//2 -a[2]//2)))


