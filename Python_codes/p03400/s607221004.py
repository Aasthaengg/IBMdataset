N = int(input())
D,X = (int(T) for T in input().split())
A = [int(input()) for T in range(0,N)]
print(X+sum(1+(D-1)//T for T in A))