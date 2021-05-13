n = int(input())
l = [list(map(int,input().split())) for i in range(n)]
a,b = [list(i) for i in zip(*l)]
m = a.index(max(a))
print(a[m] + b[m])