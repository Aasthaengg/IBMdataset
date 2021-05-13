import sys
N=int(input())
H=list(map(int,input().split()))
for i in range(1,N):
    if H[i-1]<=H[i]:
        pass
    elif H[i-1]==H[i]+1:
        H[i]+=1
    else:
        print("No")
        sys.exit()
print("Yes")