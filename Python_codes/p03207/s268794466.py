max=0
n=int(input())
k=0
for i in range(n):
    p=int(input())
    if p>=max:max=p
    k=k+p
print((k-max)+(max//2))
