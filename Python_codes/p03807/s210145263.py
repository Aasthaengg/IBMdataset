def solve():

    N = int(input())
    A = list(map(int, input().split()))

    Odd = 0

    for i in range(N):
        if A[i]%2 == 1:
            Odd += 1

    if Odd%2 == 0:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    solve()
