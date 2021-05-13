n=3
a=[0]*n
a[:]=map(int,input().split())
a.sort()
print(sum(a)-a[len(a)-1])