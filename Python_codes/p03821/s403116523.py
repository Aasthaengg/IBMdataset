N=int(input())
r=[]
bi=[]
for i in range(N):
    a,b=map(int,input().split())
    bi.append(b)
    if a%b==0:
        r.append(0)
    else:
        r.append(b-a%b)
push=0
bi=bi[::-1]
r=r[::-1]
for i in range(N):
    if i==0:
        push=r[i]
    else:
        push+=(r[i]-push)%bi[i]
print(push)