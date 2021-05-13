k,t = map(int,input().split())
ans = 0
l = list(map(int,input().split()))
m = max(l)
if m > k//2:
    if k%2:
        print(max(0,m-(k-m)-1))
    else:
        print(m-(k-m)-1)
else:
    print(0)