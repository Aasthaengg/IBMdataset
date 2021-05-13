max=0
k=0
N=int(input())
for i in range(1,N+1):
    p=int(input())
    if p>max:max=p
    k=k+p
print((k-max)+(max//2))