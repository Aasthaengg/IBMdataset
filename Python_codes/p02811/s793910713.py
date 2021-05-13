def solve():
    N, M = map(int, input().split())
    return 'Yes' if N*500 >= M else 'No'

print(solve())