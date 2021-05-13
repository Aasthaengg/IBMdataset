n = int(input())
d = list(map(int,input().split()))
d = sorted(d)
a = d[n//2-1:n//2+1]
print(a[1]-a[0])