A, B, C = map(int, input().split())

print(min(A*B//2, B*C//2, C*A//2))