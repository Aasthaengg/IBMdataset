n=int(input())
d=list(map(int,input().split()))

d.sort()
large=d[int(n/2)]
small=d[int(n/2)-1]
print(large-small)
