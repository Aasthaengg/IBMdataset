N=int(input())
*A,=map(int,input().split())
C=sum(a<0 for a in A)
B=[abs(a)for a in A]
if C%2==0:
    print(sum(B))
else:
    print(sum(B)-2*min(B))