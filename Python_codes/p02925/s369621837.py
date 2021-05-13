from collections import deque
n=int(input())
a=[]
for i in range(n):
    a.append(deque(map(lambda x:int(x)-1,input().split())))

nofrag=False
last=[0]*n
for i in range(n):
    stack=[(i,j) for j in list(a[i])[::-1]]
    check=[0]*n
    while stack:
        me,to=stack[-1]
        if a[to][0]==me:#お互いにpop
            a[to].popleft()
            a[me].popleft()
            day=max(last[me],last[to])+1
            last[to]=day
            last[me]=day
            stack.pop()
            check[me]=0
        else:#stackに追加し、自分のチェックもいれる
            if check[to]:#不可能
                nofrag=True
                break
            check[me]=1
            stack.append((to,a[to][0]))
    if nofrag:
        break

if nofrag:
    print(-1)
else:
    print(max(last))