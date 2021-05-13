A, B = map(int, input().split())

ans = max(A+(A-1), A+B, B+(B-1))
print(ans)