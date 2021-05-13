n,m = map(int,input().split())
l,r = map(int,input().split())

for i in range(m-1):
    
    nl,nr = map(int,input().split())
    if l<nl :
        l = nl
    if r > nr:
        r = nr
print(max(r-l + 1, 0))
