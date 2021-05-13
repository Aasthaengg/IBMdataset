n=int(input())
mx=0
k=0
for i in range(n):
    p=int(input())
    if p>=mx:
       mx=p
    k=k+p
print(k-mx//2)