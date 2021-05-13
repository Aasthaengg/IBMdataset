N=int(input())
*P,=map(int,input().split())

mi=P[0]
cnt=0
for i in range(N):
    if P[i]<mi:mi=P[i]
    if P[i]<=mi:cnt+=1
       
print(cnt)