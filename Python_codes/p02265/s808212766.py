from collections import deque

def pr(A,n):
    for i in range(n):
        if i!=n-1:
            print(A[i],end=" ")
        else:
            print(A[i])

n=int(input())
que_r=deque()
data=deque()

for i in range(n):
    s=input()
    l=len(s)
    if s[0]=="i":
        que_r.appendleft(s[7:])
    elif s[6]==" ":
        try:
            que_r.remove(s[7:])
        except: pass
    elif l>10:
        que_r.popleft()
    elif l>6:
        que_r.pop()

pr(que_r,len(que_r))
