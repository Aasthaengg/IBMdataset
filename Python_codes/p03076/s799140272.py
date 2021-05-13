from itertools import permutations

def f(a,g):
    return ((a+(g-1))//g)*g

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())

P=[A,B,C,D,E]
Q=permutations(P)

M=10**100
for (v,w,x,y,z) in Q:
    M=min(M,f(v,10)+f(w,10)+f(x,10)+f(y,10)+z)
print(M)
