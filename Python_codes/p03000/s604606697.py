n,x = map(int,input().split())
L = list(map(int,input().split()))

c=1
suml=0
for i in range(n):
    if x>=L[i]+suml :
        c+=1
        suml+=L[i]
    else:
        break
print(c)