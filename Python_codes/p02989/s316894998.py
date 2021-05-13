n = int(input())
d = list(map(int, input().split()))
d.sort()
num = 0
n3 = n//2
n2 = n3-1
if d[n2] == d[n3]:
    print(0)
else:
    for i in range(d[n2],d[n3]):
        num += 1
    print(num)