N=int(input())
H=list(map(int,input().split()))
H.append(10**9+1)
c=0
m=0
for i in range(N):
    if H[i]<H[i+1]:
        m=max(m,c)
        c=0
        continue
    else:
        c+=1
print(m)