N, M = map(int, input().split())
A=[int(x) for x in input().split()]
ans=N-sum(A)
print(ans if ans>=0 else -1)