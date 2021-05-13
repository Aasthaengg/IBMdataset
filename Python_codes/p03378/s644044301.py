N,M,X = (int(T) for T in input().split())
A = [int(T) for T in input().split()]
Gate = [0]*(N+1)
for T in A:
    Gate[T] += 1
print(min(sum(Gate[:X]),sum(Gate[(X+1):])))