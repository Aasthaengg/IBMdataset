#!/usr/bin/python3

import sys
sys.setrecursionlimit(10 ** 5 + 10)
def input(): return sys.stdin.readline().strip()

def resolve():
    
    N=int(input())
    x=0
    y=0
    z=0
    cnt=0
    for i in range(N):
        s=str(input())
        if s[0]=='B' and s[-1]=='A':
            x+=1
        if s[0]=='B' and s[-1]!='A':
            y+=1
        if s[0]!='B' and s[-1]=='A':
            z+=1

        
        for j in range(len(s)-1):
            if s[j:j+2]=='AB':
                cnt+=1
    if x==0:
        print(cnt+min(y,z))
    elif y>0 or z>0: print(cnt+(x-1)+min(y,z)+1)
    else: print(cnt+(x-1)+min(y,z))    
        

    
resolve()