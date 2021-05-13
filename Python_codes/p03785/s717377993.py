n,c,k=map(int,input().split())
buscount=1
waiting=0
T=[]
for _ in range(n):
    t=int(input())
    T.append(t)
T=sorted(T)
mae_no_time=T[0]
noruhito=1
for i in range(1,n):
    waiting+=T[i]-mae_no_time
    noruhito+=1
    mae_no_time=T[i]
    if waiting>k or noruhito>c:
        buscount+=1
        waiting=0
        noruhito=1

print(buscount)
