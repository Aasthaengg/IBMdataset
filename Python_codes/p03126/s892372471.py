N, M = map(int, input().split())
s = set()
for i in range(N):
    K, *A = map(int, input().split())
    if i == 0:
        s = set(A)
    else:
        t = set(A)
        s = s.intersection(t)
print(len(s))