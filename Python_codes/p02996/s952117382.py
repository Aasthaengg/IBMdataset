N=int(input())
W=[list(map(int,input().split())) for i in range(N)]
W=sorted(W,key=lambda x:x[1])
t=0

for a,b in W:
    t+=a
    if t>b:
        print("No")
        break
else:
    print("Yes")