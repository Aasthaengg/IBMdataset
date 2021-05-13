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
    N=list(map(int,list(input())))
    for i in range(1,len(N)):
        if N[i]!=9:
            ans=N[0]-1+9*(len(N)-1)
            break
    else:
        ans=N[0]+9*(len(N)-1)
    print(ans)
        

if __name__ == '__main__':
    main()
