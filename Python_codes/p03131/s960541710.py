import sys

K,A,B=map(int,input().split())

if B-A<=2:
    print(K+1)
    sys.exit()

S=A
K-=A-1
S+=(B-A)*(K//2)
if K%2:
    S+=1
print(S)
