k=int(input())
a=[]
print(50)
n=k%50
m=k//50
for i in range(n):
    a.append(100+m-n)
for i in range(50-n):
    a.append(49+m-n)
print(*a)