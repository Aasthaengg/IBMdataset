# A - Remaining Time
A, B = map(int,input().split())
ans = A + B
if ans >= 24:
    ans = ans - 24
else:
    pass
print(ans)