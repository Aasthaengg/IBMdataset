n=int(input())
d=sorted(list(map(int,input().split())))
print(max(0, d[n//2]-d[n//2-1]))
