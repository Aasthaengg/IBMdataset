n=int(input())
l=list(map(int,input().split()))
b=[]
z=l[0]
for i in range(1,len(l)):
    z=z^l[i]
for i in range(n):
    b.append(z^l[i])
print(*b)
