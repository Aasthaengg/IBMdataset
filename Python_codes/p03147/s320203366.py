def garden(a,h):
    if len(a)==0:
        return 0
    m=min(a)
    i=a.index(m)
    return m-h+garden(a[:i],m)+garden(a[i+1:],m)
n=input()
print(garden(list(map(int,input().split())),0))