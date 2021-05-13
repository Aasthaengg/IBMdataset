def main():
    A, B = map(int, input().split())
    A, B = max(A, B), min(A, B)
    return A + max(A-1, B)
print(main())
