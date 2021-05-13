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
    A,B=map(int,input().split())
    ans=[['#']*100 for _ in range(50)]+[['.']*100 for _ in range(50)]
    A-=1
    B-=1
    y,x=1,1
    for _ in range(A):
        ans[y][x]='.'
        x+=2
        if x>=100:
            if x%2:
                y+=1
                x=2
            else:
                y+=2
                x=1
    y,x=51,1
    for _ in range(B):
        ans[y][x]='#'
        x+=2
        if x>=100:
            if x%2:
                y+=1
                x=2
            else:
                y+=2
                x=1
    print(100,100)
    for row in ans:
        print(''.join(row))
    

if __name__ == '__main__':
    main()
