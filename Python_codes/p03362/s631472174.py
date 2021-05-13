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
    def is_prime(x):
        for i in range(2,int(x**0.5)+1):
            if x%i==0:
                return False
        return True
    N=int(input())
    ans=[]
    tmp=1
    while len(ans)<N:
        tmp+=10
        if is_prime(tmp):
            ans.append(tmp)
    print(*ans)
    

if __name__ == '__main__':
    main()
