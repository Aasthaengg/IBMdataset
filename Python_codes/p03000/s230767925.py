N,X = (int(x) for x in input().split())
L = [int(x) for x in input().split()]
Bound = sum(sum(L[:x])<=X for x in range(0,N+1))
print(Bound)