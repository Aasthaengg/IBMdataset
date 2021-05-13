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
    s=input()
    K=int(input())
    l=[]
    for i in range(len(s)):
        for j in range(1,K+1):
            if i+j>len(s):
                continue
            l.append(s[i:i+j])
    l=list(set(l))
    l.sort()
    print(l[K-1])

if __name__ == '__main__':
    main()
