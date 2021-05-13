A, B, K = map(int, input().split())
r = []
for i in range(A, min(A+K, B+1)):
    r.append(i)
for i in range(max(B-K+1, A), B+1):
    r.append(i)
for i in sorted(list(set(r))):
    print(i)
