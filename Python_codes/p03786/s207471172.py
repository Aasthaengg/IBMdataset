n = int(input())
a = sorted(list(map(int,input().split())))
imp = -1
size = 0

for i in range(n-1):
    size += a[i]
    if size*2 < a[i+1]:
        imp = i

print(n-imp-1)