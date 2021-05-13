from collections import deque
S=list(map(lambda x: 1 if x=="T" else 0,input()))

q=deque()

for i in S:

    if i:
        if (not q) or q[-1]!=0:
            q.append(i)
        elif q and q[-1]==0:
            q.pop()
    else:
        q.append(i)
print(len(q))