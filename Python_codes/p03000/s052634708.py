n,x = list(map(int, input("").split()))
l=list(map(int, input("").split()))
d=0
k=1
for i in l:
    d+=i
    if d <=x :
        k+=1
    else:
        break
print(k)