# coding: utf-8
# Your code here!
N=int(input())

pre_T=0
pre_A=0

def krag(n,m):
    return -(-n//m)


for _ in range(N):
    T,A=map(int,input().split())
    
    if T<pre_T or A<pre_A:
        k=max(krag(pre_T,T),krag(pre_A,A))
        T*=k
        A*=k
    
    pre_T,pre_A=T,A    
print(T+A)