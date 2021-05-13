A, B, C = list(map(int, input().split()))
ans = "No"
if A == B:
    if B != C:
        ans = "Yes"
elif A == C or B == C:
    ans = "Yes"
print(ans)
