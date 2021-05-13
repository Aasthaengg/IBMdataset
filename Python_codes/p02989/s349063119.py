N = int(input())
D = sorted(list(map(int,input().split())))
l = D[N//2-1]
r = D[N//2]
print(r-l)