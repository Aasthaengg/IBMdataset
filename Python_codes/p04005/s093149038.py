t = list(map(int,input().split()))

t.sort()

if t[-1]%2==0:
    print(0)
else:
    print(t[0]*t[1])