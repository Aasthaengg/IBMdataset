inpl = lambda: list(map(int,input().split()))
N, A, B = inpl()
print(min(A,B), max(0, A+B-N))