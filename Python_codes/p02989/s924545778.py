N = int(input())
d = list(map(int, input().split()))
d.sort()

idx1 = N//2-1
idx2 = N//2
print(d[idx2]-d[idx1])