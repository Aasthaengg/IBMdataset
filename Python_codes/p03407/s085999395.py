def solve():
  A, B, C = map(int, input().split())
  return 'Yes' if A + B >= C else 'No'

print(solve())
