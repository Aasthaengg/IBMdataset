#13
N = int(input())
d = list(map(int,input().split()))
h = 0

d.sort()

h = int(N/2)

print(d[h]-d[h-1])