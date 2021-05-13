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
    S=list(input())
    A,C,Q=[0]*(len(S)+1),[0]*(len(S)+1),[0]*(len(S)+1)
    l_B=[]
    l_Q=[]
    q=0
    for i in range(len(S)):
        A[i+1]=A[i]+(S[i]=='A')
        C[i+1]=C[i]+(S[i]=='C')
        Q[i+1]=Q[i]+(S[i]=='?')
        if S[i]=='?':
            q+=1
            l_Q.append(i)
        if S[i]=='B':
            l_B.append(i)
    ans=0
    pow3q=pow(3,q,MOD)
    if q-1>=0:
        pow3q_1=pow(3,q-1,MOD)
    else:
        pow3q_1=0
    if q-2>=0:
        pow3q_2=pow(3,q-2,MOD)
    else:
        pow3q_2=0
    if q-3>=0:
        pow3q_3=pow(3,q-3,MOD)
    else:
        pow3q_3=0
    
    for x in l_B:
        ans+=A[x]*(C[len(S)]-C[x+1])*pow3q
        ans+=Q[x]*(C[len(S)]-C[x+1])*pow3q_1
        ans+=A[x]*(Q[len(S)]-Q[x+1])*pow3q_1
        ans+=Q[x]*(Q[len(S)]-Q[x+1])*pow3q_2
        ans%=MOD
    for x in l_Q:
        ans+=A[x]*(C[len(S)]-C[x+1])*pow3q_1
        ans+=Q[x]*(C[len(S)]-C[x+1])*pow3q_2
        ans+=A[x]*(Q[len(S)]-Q[x+1])*pow3q_2
        ans+=Q[x]*(Q[len(S)]-Q[x+1])*pow3q_3
        ans%=MOD        
    print(ans)
    

if __name__ == '__main__':
    main()
