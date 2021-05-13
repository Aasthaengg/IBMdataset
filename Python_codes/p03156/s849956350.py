N=int(input())
A,B=map(int,input().split())
P=list(map(int,input().split()))

q1=len([i for i in range(N) if P[i]<=A])
q2=len([i for i in range(N) if A<P[i]<=B])
q3=len([i for i in range(N) if B<P[i]])

ans=min(q1,q2,q3)
print(ans)