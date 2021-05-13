# ABC158 B - Count Balls
N,A,B=map(int,input().split())

# Aが青で,Bが赤
C =A*(N//(A+B))
if N%(A+B) <A:
    D = N%(A+B)
else:
    D = A
print(C+D)