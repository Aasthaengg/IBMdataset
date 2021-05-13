a = [int(i) for i in input().split()]
k = int(input())

for i in range(k):
    idx = a.index(max(a[0], a[1], a[2]))
    a[idx] *= 2
print(sum(a))