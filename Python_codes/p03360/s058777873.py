a = [int(i) for i in input().split()]
k = int(input())
a.sort()
for i in range(k):
    a[2] *= 2
print(sum(a))