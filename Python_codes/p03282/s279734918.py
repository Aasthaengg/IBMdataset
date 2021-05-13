from collections import deque
S=deque(list(map(int,list(input()))))
K=int(input())
i=0
while S:
    if S[0]==1:
        S.popleft()
        i+=1
    else:
        break
result=1 if K<=i else S[0]
print(result)  