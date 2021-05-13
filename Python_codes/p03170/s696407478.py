# coding: utf-8
# Your code here!
N,K=map(int,input().split())
A=list(map(int,input().split()))

dp=[0]*(K+1)

for i in range(K+1):    
    for a in A:
        if i+a<=K:
            if dp[i]==0:
                dp[i+a]=1

print("First" if dp[-1]==1 else "Second")
