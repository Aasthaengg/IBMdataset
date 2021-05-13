import sys
input=sys.stdin.readline

N=int(input())
A=list(map(int,input().split()))
a=0
b=0
left=0
right=0
res=0
while(left<N):
    while(right<N and a+A[right]==b^A[right]):
        a+=A[right]
        b^=A[right]
        right+=1
    res+=(right-left)
    a-=A[left]
    b^=A[left]
    left+=1
print(res)
