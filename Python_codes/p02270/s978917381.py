n,k=map(int,input().split())
w=[int(input())for i in range(n)]

def check(x):
    global w
    global n,k
    track=0
    now=0
    for i in w:
        if i>x:
            return False
        if now+i>x:
            track+=1
            now=i
        else:
            now+=i
    if now>0:
        track+=1
    if track>k:
        return False
    else:
        return True
amax=1000000000
amin=0
while amin+1!=amax:
    amid=(amax+amin)//2
    if check(amid):
        amax=amid
    else:
        amin=amid
    
print(amax)
