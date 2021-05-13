N=int(input())
Vlist=list(map(int, input().split()))
Clist=list(map(int, input().split()))

ret=0

for i in range(N):
    if Vlist[i]-Clist[i] > 0:
        ret += Vlist[i]-Clist[i]
print(ret)