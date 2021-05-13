import sys
input=sys.stdin.readline
N=int(input())
A=list(map(int,input().split()))
A.sort()
ans=[]

if A[0]>0:
    num=A[0]
    for i in range(1,N-1):
        ans.append([num,A[i]])
        num-=A[i]
    ans.append([A[-1],num])
    print(A[-1]-num)
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
elif A[-1]<0:
    A.sort(reverse=True)
    num=A[0]
    for i in range(1,N):
        ans.append([num,A[i]])
        num-=A[i]
    print(num)
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
else:
    M=A[-1]
    m=A[0]
    for i in range(1,N-1):
        if A[i]<0:
            ans.append([M,A[i]])
            M-=A[i]
        else:
            ans.append([m,A[i]])
            m-=A[i]
    ans.append([M,m])
    print(M-m)
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])