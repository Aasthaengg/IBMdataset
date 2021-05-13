A, B, X = map(int, input().split())

ans = 'YES' if A <= X and X <= A + B else 'NO'
print(ans)
