def solve():
    H,N = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    A_sum = sum(A)
    if A_sum >= H:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()