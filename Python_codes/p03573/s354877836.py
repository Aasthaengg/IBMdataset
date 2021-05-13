def solve():
    A, B, C = map(int, input().split())
    if A == B:
        print(C)
    elif B != C:
        print(B)
    else:
        print(A)



if __name__ == "__main__":
    solve()