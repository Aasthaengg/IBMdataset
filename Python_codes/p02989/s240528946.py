n = int(input())
d = sorted(list(map(int, input().split())))
l,r = d[n//2-1], d[n//2]
print(r-l)