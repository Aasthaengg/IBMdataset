from collections import deque
n=int(input())
b=list(map(int,input().split()))
a=[]
while b:
    maxpoint=0
    for i in range(len(b)):
        if i+1==b[i]:
            maxpoint=max(maxpoint, i+1)
    if maxpoint==0:
        print(-1)
        exit()
    else:
        a.append(maxpoint)
        b=b[:maxpoint-1]+b[maxpoint:]

for i in range(len(a)):
    print(a[-i-1])