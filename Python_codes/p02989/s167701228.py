n = int(input())
d = list(map(int,input().split()))
d = sorted(d)
a = d[n//2] - d[n//2-1]
print(a)
