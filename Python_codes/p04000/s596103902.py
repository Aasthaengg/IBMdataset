# -*- coding: utf-8 -*-
import sys
sys.setrecursionlimit(10**9)
INF=10**18
MOD=10**9+7
input=lambda: sys.stdin.readline().rstrip()
YesNo=lambda b: bool([print('Yes')] if b else print('No'))
YESNO=lambda b: bool([print('YES')] if b else print('NO'))
int1=lambda x:int(x)-1

def main():
    H,W,N=map(int,input().split())
    s=set()
    for i in range(N):
        s.add(tuple(map(int1,input().split())))
    ans=[0]*10
    used=set()
    for y,x in s:
        for dy in range(-1,2):
            for dx in range(-1,2):
                if 0>y+dy-1 or y+dy+1>=H or 0>x+dx-1 or x+dx+1>=W or (y+dy,x+dx) in used:
                    continue
                tmp=0
                used.add((y+dy,x+dx))
                for ddy in range(-1,2):
                    for ddx in range(-1,2):
                        if (y+dy+ddy,x+dx+ddx) in s:
                            tmp+=1
                ans[tmp]+=1
    ans[0]=(H-2)*(W-2)-sum(ans[1:])
    for row in ans:
        print(row)
    
    

if __name__ == '__main__':
    main()
