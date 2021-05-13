def solve():
    S = input()
    T = input()
    expected_T = S + T[-1]
    if expected_T == T:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()