n = int(input())
a = [int(x) - i for i, x in enumerate(input().split())]
a.sort()
mid = a[n//2]
print(sum([abs(mid - a[i]) for i in range(n)]))
