N = int(input())
xy = [list(map(int,input().split())) for i in range(N)]
xy = [list(x) for x in zip(*xy)]
a = [i+j for i,j in zip(xy[0],xy[1])]
b = [i-j for i,j in zip(xy[0],xy[1])]
aa = max(a) - min(a)
ba = max(b) - min(b)
print(max(aa,ba))