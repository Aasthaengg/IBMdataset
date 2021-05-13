N=int(input())
K=int(input())
num=1
for i in range(1,N+1):
    if num<=K:
        num*=2
    else:
        num+=K
print(num)