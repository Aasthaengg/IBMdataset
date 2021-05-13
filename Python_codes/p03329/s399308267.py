import queue

n=int(input())

sixexp=[6**i for i in range(1,7)]
nineexp=[9**i for i in range(1,6)]

lis=[1]+sixexp+nineexp

q=queue.Queue()

numlist=[0 for i in range (n+1)]

c=0
while c!=n:
    for i in lis:
        if c+i<=n:
            if numlist[c+i]==0:
                q.put(c+i)
                numlist[c+i]=numlist[c]+1
    c=q.get()
print(numlist[n])