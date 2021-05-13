N = int(input())
d = list(map(int, input().split()))
d.sort()
mid1 = d[N//2-1]
mid2 = d[N//2]
print(mid2-mid1)