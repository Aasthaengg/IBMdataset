N,T=map(int,input().split())
X=list(map(int,input().split()))+[float("inf")]

A=0
B=0
S=0
for t in X:
    if B<t:
        S+=B-A
        A=t
    B=t+T

print(S)
