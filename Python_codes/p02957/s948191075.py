A, B = list(map(int, input().split()))

C = A + B
ans = C // 2 if C % 2 == 0 else "IMPOSSIBLE"
print(ans) 