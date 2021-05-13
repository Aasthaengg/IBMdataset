a = [i for i in map(int, input().split())]
a.sort()
ans = (a[1] - a[0]) + (a[2] - a[1])
print(ans)