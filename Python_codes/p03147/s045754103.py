n=int(input())
h=list(map(int,input().split()))
m=0
s=0
for j in range(100):
    for i in range(n):
        if h[i]==0:
            s=0
        elif s!=0:
            h[i]-=1
        else:
            h[i]-=1
            s+=1
            m+=1
    s=0
print(m)