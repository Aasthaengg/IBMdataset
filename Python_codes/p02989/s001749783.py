N = int(input().rstrip())
d = list(map(int,input().rstrip().split()))
d.sort()
print(d[N//2]-d[N//2-1])