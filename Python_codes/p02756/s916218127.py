S=input()
N=int(input())

from collections import*
D=deque(S)
count=0
for _ in range(N):
    *Q,=input().split()
    if len(Q)==1:
        count+=1
    else:
        if (count+int(Q[1]))%2:
            D.appendleft(Q[2])
        else:
            D.append(Q[2])
ans=''.join(D)
print(ans[::-1] if count%2 else ans)