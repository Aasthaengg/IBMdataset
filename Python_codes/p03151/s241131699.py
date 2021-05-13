N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
if sum(A)<sum(B):
    print(-1)
else:
    a=0
    s=0
    l=[]
    for i in range(N):
        if A[i]<B[i]:
            a+=1
            s+=B[i]-A[i]
        else:
            l.append(A[i]-B[i])
    l.sort(reverse=1)
    for i in range(len(l)):
        if s<=0:
            break
        s-=l[i]
        a+=1
    print(a)