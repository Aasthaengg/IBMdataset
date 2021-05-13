N = int(input())
p = list(map(int,input().split()))
p = sorted(p)
c = p[N//2-1]
d = p[N//2]
print(d-c)