def solve():
    N = int(input())
    A = [int(i) for i in input().split()]
    sorted_A = sorted(A, reverse=True)
    cnt = N
    ptr = 0
    is_first = True
    ans = 0
    while cnt > 0:
        ans += sorted_A[ptr]
        if is_first:
            is_first = False
        else:
            ptr +=1
            is_first = True
        cnt -= 1
    print(ans - sorted_A[0])

if __name__ == "__main__":
    solve()