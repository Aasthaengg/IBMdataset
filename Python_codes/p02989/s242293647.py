n = int(input())
d = [int(i) for i in input().split()]
d2 = sorted(d)
p = n // 2
print(d2[p] - d2[p-1])