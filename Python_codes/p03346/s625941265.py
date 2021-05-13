n=int(input())
p=[int(input()) for _ in range(n)]
q=[0]*(n+1)

for i in range(n):
    q[p[i]]=i+1
cnt=1
curcnt=0
for i in range(1,n+1):
    if q[i]>q[i-1]:
        curcnt+=1
        cnt=max(cnt,curcnt)
    else:
        curcnt=1

print(n-cnt)