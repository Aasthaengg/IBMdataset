N = int(input())
a = list(map(int, input().split()))


a = set(a)
a = list(a)
a = sorted(a)

SUM = 0
for i in range(len(a)-1):
    SUM = SUM + (a[i+1]-a[i])
print(SUM)