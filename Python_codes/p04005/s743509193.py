A, B, C = map(int, input().split())
if max(A, B, C) % 2 == 0:
    ans = 0
else:
    ans = min(A, B, C)*(A+B+C-max(A, B, C)-min(A, B, C))
print(ans)
