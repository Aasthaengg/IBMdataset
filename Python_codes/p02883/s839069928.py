import sys

input=sys.stdin.readline

N,K=map(int,input().split())
A=list(map(int,input().split()))
F=list(map(int,input().split()))

A.sort()
F.sort(reverse=True)

def condition(num):
    count=0
    goal=[num//F[i] for i in range(N)]
    for i in range(0,N):
        if A[i]>goal[i]:
            count+=A[i]-goal[i]
    return K>=count

start=0
end=2*(10**17)
while end-start>1:
    test=(end+start)//2
    if condition(test):
        end=test
    else:
        start=test

if condition(start):
    print(start)
else:
    print(end)