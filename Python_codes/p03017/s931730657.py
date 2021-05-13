import sys
from collections import defaultdict
#n=int(input())
n,a,b,c,d=map(int,input().split())
#a=[int(i) for i in input().split()]
s='_'+input()

ans=['Yes','No']

#print(s,n,a,b,c,d)

def CanGo(x,y):
    cnt=0
    root=s[x:y]
    for c in root:
        if c=='#':
            cnt+=1
        elif c=='.':
            if cnt>2:
                return False
            cnt=0
    return True


def CanPass(x,y):  #(b,d)
    root=s[x-1:y+2]
    '''
    q=s[x-1:x+2]
    print(root,q)
    print(root,len(root)-3+1)
    for i in range(len(root)-3+1):
        if q=='...':
            return True
        q=q[1:3]+s[x+3+i]
    '''
    if root.find('...')!=-1:
        return True
    return False
        


if c<d:
    if CanGo(b,d) and CanGo(a,c):
        ai=0
    else:
        ai=1
elif c>d:
    if CanGo(b,d) and CanGo(a,c) and CanPass(b,d):
        ai=0
    else:
        ai=1
    
    

print(ans[ai])
