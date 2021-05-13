A, B, C, K = map(int, input().split())
ans = A-B
if K % 2 != 0: ans *= -1 
print("Unfair" if abs(B-A) >= 10 ** 18 else ans)