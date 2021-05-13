def solve():
    A, B, _, K = [int(i) for i in input().split()]
    if abs(A - B) > 10 ** 18:
        print('Unfair')
        exit()
    if K % 2 == 0:
        print(A - B)
    else:
        print(B - A)

if __name__ == "__main__":
    solve()