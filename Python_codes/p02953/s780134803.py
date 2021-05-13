N=int(input())
H=list(map(int,input().split()))
hlow=[H[i]-1 for i in range(N)]
a=[hlow[0]]
flag=True
for i in range(1,N):
    if a[i-1]<=hlow[i]:
        a.append(hlow[i])
    elif a[i-1]<=H[i]:
        a.append(H[i])
    else:
        print('No')
        flag=False
        break

if flag:
    print('Yes')