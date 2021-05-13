A, B, C = map(int, input().split())
ans = A
if A == B: ans = C
if A == C: ans = B
print(ans)