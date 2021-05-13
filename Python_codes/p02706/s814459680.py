N , M = (int(a) for a in input().split())
A = list(map(int,input().split()))
d = sum(A)
print(max(N-d,-1))