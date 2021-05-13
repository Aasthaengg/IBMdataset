s = 0
n = input()
a = map(int,raw_input().split())
a.sort()
for i in range(0,n):
    s += a[i]
print a[0],a[n-1],s