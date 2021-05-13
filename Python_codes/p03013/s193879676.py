N,M = map(int,input().split())
a = [0]*(N+2)
pass_list = [0]*(N+2)

for i in range(M):
    b = int(input())
    a[b] = 1
if(a[1] !=1):
    pass_list[1]=1
if(a[2] !=1):
    pass_list[2]=1
for i in range(2,N+1):
    if(a[i] != 1):
        pass_list[i] += pass_list[i-1]+pass_list[i-2]
print(pass_list[N]%1000000007)
