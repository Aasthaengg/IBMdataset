n=int (input())
d= list(map(int, input().strip().split()))
d.sort()
s=d[n//2-1]
t=d[n//2]
print(t-s)
