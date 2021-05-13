N,K=map(int, input().split())
A=list(map(int, input().split()))
A=sorted(A)[::-1]
print(sum(A[:K]))