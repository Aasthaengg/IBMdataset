N=int(input())
d=list(map(int,input().split()))
d.sort()
print(max(0,d[N//2]-d[N//2-1]))