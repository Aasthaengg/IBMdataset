n,k = map(int,input().split())
l = [0]*(10**5+1)
for i in range(n):
    ai,bi = map(int,input().split())
    l[ai]+=bi
for index,i in enumerate(l):
    if i:
        k-=i
        if k<=0:
            break
print(index)