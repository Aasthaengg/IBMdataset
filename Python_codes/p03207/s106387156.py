n=int(input())
ar=[]
for i in range(n):
    ar.append(int(input()))
k=max(ar)
print(sum(ar)-(k//2))
