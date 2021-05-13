N,M = map(int,input().split())

l = 0
r = 10**12+1

while r-l>1:
    s = (r+l)//2#作るべきsとc
    c = 2*s
    t = s

    S,C = N,M
    s-=S#Sは全部使った
    if s > 0:
        C-=2*s
    if C < c:
        r = t
    else:
        l = t
    
print(l)