from collections import deque
K=int(input())
lunlun=[]
q=deque(list(range(1,10)))
while 1:
    r=q.popleft()
    lunlun.append(r)
    n=str(r)[-1]
    if n!='0':
        q.append(r*10+int(n)-1)
    q.append(r*10+int(n))
    if n!='9':
        q.append(r*10+int(n)+1)
    if len(lunlun)>K:
        break
print(lunlun[K-1])