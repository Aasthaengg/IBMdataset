A, B, K = map(int, input().split())

ans = set()
for i in range(A, min(B + 1, A + K)):
    ans.add(i)

for i in range(max(A, B - K + 1), B + 1):
    ans.add(i)
ans = sorted(list(ans))
for i in ans:
    print(i)
