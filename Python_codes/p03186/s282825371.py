A, B, C = map(int, input().split())
ans = B
ans += min(C, A+B+1)
print(ans)