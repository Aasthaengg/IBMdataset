N=int(input())
A=list(map(int,input().split()))
ans=[]
B=0
P=0
if abs(max(A))>=abs(min(A)):
    #print("A")
    B=max(A)
    for i in range(N):
        if A[i]==max(A):
            B=A[i]
            P=i
    for i in range(1,N):
        if A[i-1]<=A[i]:
            pass
        else:
            A[i]+=B
            ans.append([P+1,i+1])
            if B<A[i]:
                B=A[i]
                P=i
            if A[i-1]<=A[i]:
                pass
            else:
                A[i]+=B
                ans.append([P+1,i+1])
                if B<A[i]:
                    B=A[i]
                    P=i
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
else:
    B=min(A)
    for i in range(N):
        if A[i]==min(A):
            B=A[i]
            P=i
    #print(B,P)
    for i in range(N-1):
        #print(A,B)
        if A[N-2-i]<=A[N-1-i]:
            pass
        else:
            A[N-2-i]+=B
            ans.append([P+1,N-1-i])
            if B>A[N-2-i]:
                B=A[N-2-i]
                P=N-2-i
            if A[N-2-i]<=A[N-i-1]:
                pass
            else:
                A[N-2-i]+=B
                ans.append([P+1,N-1-i])
                if B>A[N-2-i]:
                    B=A[N-2-i]
                    P=N-2-i
    print(len(ans))
    for i in range(len(ans)):
        print(ans[i][0],ans[i][1])
#print(A)