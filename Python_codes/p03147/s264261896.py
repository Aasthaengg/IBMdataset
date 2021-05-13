n=input()
def garden(a,h):
    if len(a)==0:
        return 0
    if len(a)==1:
        return a[0]-h
    m=min(a)
    i=a.index(m)
    return m-h+garden(a[:i],m)+garden(a[i+1:],m)
print(garden(list(map(int,input().split())),0))