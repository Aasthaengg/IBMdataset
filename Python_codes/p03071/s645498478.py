A, B = map(int, input().split())
if A > B:
    ans = A
    A -= 1
else:
    ans = B
    B -= 1
ans += max(A, B)
print(ans)