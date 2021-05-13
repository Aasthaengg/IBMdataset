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
    sx,sy,tx,ty=map(int,input().split())
    ans=''
    ans+='R'*(tx-sx)+'U'*(ty-sy)
    ans+='L'*(tx-sx)+'D'*(ty-sy)
    ans+='D'+'R'*(tx-sx+1)+'U'*(ty-sy+1)+'L'
    ans+='U'+'L'*(tx-sx+1)+'D'*(ty-sy+1)+'R'
    print(ans)
    

if __name__ == '__main__':
    main()
