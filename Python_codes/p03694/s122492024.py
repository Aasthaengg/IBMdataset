n = int(input())
a = [int(i) for i in input().split()]
a = sorted(a)
print(a[n-1]-a[0])