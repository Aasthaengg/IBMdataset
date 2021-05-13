import heapq

N=int(input())
A=list(map(int,input().split()))

A.sort(reverse=True)

def condition(num):
    test=A[:num]+A[num+1:]
    s=A[num]
    heapq.heapify(test)
    while test:
        x=heapq.heappop(test)
        if 2*s>=x:
            s+=x
        else:
            return False
    return True

start=0
end=N-1
while end-start>1:
    t=(end+start)//2
    if condition(t):
        start=t
    else:
        end=t

if condition(end):
    print(end+1)
elif condition(start):
    print(start+1)
else:
    print(0)