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
    S=input()
    tmp=0
    for i in range(len(S)-1):
        tmp+=(S[i+1]!=S[i])
    print(tmp)

if __name__ == '__main__':
    main()
