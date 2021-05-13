a = list(map(int, input().split()))
k = int(input())
a.sort()
print(sum(a[0:2])+a[2]*(2**k))