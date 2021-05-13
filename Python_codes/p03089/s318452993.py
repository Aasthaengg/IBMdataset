import sys
N=int(input())
b=list(map(int,input().split()))

ans=[]
for i in range(N):
    for j in range(N-1-i,-1,-1):
        if b[j]==j+1:
            ans.append(b.pop(j))
            break
        elif j==0:
            print('-1')
            sys.exit()
        else:
            continue

for i in range(N-1,-1,-1):
    print(ans[i])