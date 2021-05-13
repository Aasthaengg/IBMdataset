N=int(input())
d=list(map(int,input().split()))
d=sorted(int(i) for i in d)
print(d[N//2]-d[N//2-1])