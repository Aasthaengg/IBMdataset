n,m = map(int,input().split())
a = list(map(int,input().split()))

if len([i for i in a if i >= sum(a)/(4*m)]) >= m:
    print("Yes")
else:
    print("No")