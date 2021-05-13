A, B, K = map(int, input().split())
a = [i for i in range(A, min(A+K, B+1))]
b = [i for i in range(max(B-K+1, A), B+1)]
s = list(set(a+b))
s.sort()
for r in s:
    print(r)