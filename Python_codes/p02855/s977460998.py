from _collections import deque
h,w,k=map(int,input().split())
S=[input() for _ in range(h)]
A=deque([])
cnt=1

def func(X):
    global cnt
    ANS=[]
    c=X.count('#')
    a=0
    for x in X:
        ANS.append(cnt)
        if x=='#':
            cnt+=1
            a+=1
            if a==c:
                for _ in range(w-len(ANS)):
                    ANS.append(cnt-1)
                break
    A.append(ANS)



for i in range(h):
    if S[i].count('#')==0 and i!=0 and len(A)!=0:
        A.append(A[-1])
    elif S[i].count('#')!=0:
        func(S[i])

if len(A)!=h:
    for _ in range(h-len(A)):
        A.appendleft(A[0])

for ans in A:
    print(*ans)