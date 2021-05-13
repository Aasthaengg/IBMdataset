A,B,C=map(int,input().split())
N=int(input())
L=[A,B,C]
L=sorted(L)
print(((2**N)*L[2])+L[0]+L[1])