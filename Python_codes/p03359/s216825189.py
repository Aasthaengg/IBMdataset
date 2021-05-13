A, B = map(int, input().split())
ans = A - 1 + (1 if B >= A else 0)
print(ans)