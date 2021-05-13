N, M = map(int, input().split())
Ans = list(map(int, input().split()))
Ans = Ans[1:]
Ans = set(Ans)

for _ in range(N-1):
    A = list(map(int, input().split()))
    A = set(A[1:])
    Ans = Ans & A
print(len(Ans))