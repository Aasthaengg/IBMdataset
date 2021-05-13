import sys
input=sys.stdin.readline
a,b,m=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
L=[[int(j) for j in input().split()] for i in range(m)]

sortsec = lambda val : val[2]
L1=sorted(L,key=sortsec,reverse=True)
cnt=10**8
for i,j,k in L1:
    num=A[i-1]+B[j-1]-k
    cnt=min(cnt,num)
num=min(A)+min(B)
print(min(num,cnt))