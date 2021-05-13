A, B, C = map(int, input().split())
ans = 'No'
if A + B >= C:
    ans = 'Yes'
print(ans)