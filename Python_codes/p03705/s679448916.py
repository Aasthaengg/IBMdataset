N, A, B = map(int, input().split())
ans = 0
if A == B: ans = 1
elif A > B or N == 1: pass
else: ans = ((N-1)*(B-1)+A) - ((N-1)*(A-1)+B) + 1
print(ans)