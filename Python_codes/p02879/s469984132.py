def solve():
    A, B = map(int, input().split())
    if A<10 and B<10:
        return A*B
    return -1
print(solve())