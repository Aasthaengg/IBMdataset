A,B,M = map(int,input().split())
A_li = list(map(int,input().split()))
B_li = list(map(int,input().split()))

inf = float("inf")
posibility = inf

for m in range(M):
    x,y,c=map(int,input().split())
    tmp_posibility=A_li[x-1]+B_li[y-1]-c
    posibility=min(posibility,tmp_posibility)
 

no_c = min(A_li)+min(B_li)
decition = min(posibility,no_c)

print(decition)