def solve():
    import math
    A,B = [int(i) for i in input().split()]
    A_orig = math.ceil(A/0.08)
    A_orig_next = math.ceil((A+1)/0.08)
    B_orig = math.ceil(B/0.1)
    B_orig_next = math.ceil((B+1)/0.1)
    ans = -1
    for i in range(A_orig, A_orig_next):
        if B_orig <= i < B_orig_next:
            ans = i
            break
    print(ans)

if __name__ == "__main__":
    solve()