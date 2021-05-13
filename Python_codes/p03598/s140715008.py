N=int(input())
K=int(input())
x=list(map(int,input().split()))

num=0
for i in range(N):
    a=x[i]
    if a<=K-a:
        num+=2*a
    else:
        num+=(K-a)*2

print(num)