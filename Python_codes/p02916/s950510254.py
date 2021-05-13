N=int(input())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))+[0]
ans=0
a_p=N+1

for a in A:
    ans+=B[a-1]+C[a-2]*(a-a_p==1)
    a_p=a
print(ans)