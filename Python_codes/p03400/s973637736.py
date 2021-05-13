n=int(input())
d,x= list(map(int, input().strip().split()))
a=[0]*n
for i in range(n):
    a[i]=int(input())
choko=x
for i in range(n):
    choko+=((d-1)//a[i])+1
print(choko)