
k,t = map(int,input().split())
a = list(map(int,input().split()))

mx = max(a)

if k -mx >= mx -1:
    print(0)
else:
    print(2*mx-k-1)
