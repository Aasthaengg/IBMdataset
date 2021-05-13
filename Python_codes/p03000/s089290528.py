N,X = map(int,input().split())
L = list(map(int,input().split()))
cu=0
c=1
for i in range(N):
    cu+=L[i]
    if cu <=X:
        c+=1
    else:
        break
print(c)
