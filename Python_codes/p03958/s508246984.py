k,t = map(int,input().split())
l = list(map(int,input().split()))

if len(l) == 0:
    print(l[0]-1)
    exit()

m = max(l)
s = sum(l)-m

if m-1 > s:
    print(m-s-1)
else:
    print(0)