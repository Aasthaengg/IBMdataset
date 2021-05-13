from collections import deque
def solve1():
    print(sum(A)-min(A)*2)
    que=deque(A)
    while(len(que)>1):
        l,r=que.popleft(),que.pop()
        if que or (not que and l-r>=r-l):
            print(l,r)
            m=l-r
            que.appendleft(m)
        else:
            print(r,l)
def solve2():
    li=list(map(abs,A))
    print(sum(li)-min(li)*2)
    que=deque(A)
    while(len(que)>1):
        l,r=que.popleft(),que.pop()
        if que or (not que and r-l>=l-r):
            print(r,l)
            m=r-l
        else:
            print(l,r)
        que.append(m)
def solve3():
    li=list(map(abs,A))
    print(sum(li))
    minus,plus=[],[]
    for i in range(N):
        if A[i]>=0:
            plus.append(A[i])
        else:
            minus.append(A[i])
    mque,pque=deque(sorted(minus)),deque(sorted(plus))
    for i in range(N-1):
        m,p=mque.pop(),pque.pop()
        if i==N-2:
            print(p,m)
        else:
            if len(mque)==0:
                print(m,p)
                mque.append(m-p)
            else:
                print(p,m)
                pque.append(p-m)
N=int(input())
A=sorted(map(int,input().split()))

if min(A)>=0:
    solve1()
elif max(A)<=0:
    solve2()
else:
    solve3()