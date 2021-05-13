N, K = map(int, input().split())
S = list(input())
A = {}
if S[0] == "1":
    A[1] = 0
    c = 1
else:
    A[0] = 0
    c = 0
for i in range(N-1):
    if S[i] == "0" and S[i+1] == "1":
        c += 1
        A[c] = i+1
B = {}
c = 1
for i in range(N-1):
    if S[i] == "1" and S[i+1] == "0":
        B[c] = i
        c += 1

ans = 0
for p, v in A.items():
    t = B.get(p+K, N-1)
    ans = max(t-v+1, ans)
print(ans)