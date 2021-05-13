def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    is_approved = True
    for num in A:
        if num % 2 == 0:
            if not (num % 3 == 0 or num % 5 == 0):
                is_approved = False
    if is_approved:
        print("APPROVED")
    else:
        print("DENIED")

if __name__ == "__main__":
    solve()