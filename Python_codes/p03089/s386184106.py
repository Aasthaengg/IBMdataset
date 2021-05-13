from _collections import deque
n=int(input())
B=list(map(int,input().split()))
ANS=deque([])
cnt=0
while len(B)>0 and cnt<10**5:
    for i in reversed(range(len(B))):
        if i+1==B[i]:
            B=B[:i]+B[i+1:]
            ANS.appendleft(i+1)
            break
    cnt+=1
if len(B)==0:
    for a in ANS:
        print(a)
else:
    print(-1)