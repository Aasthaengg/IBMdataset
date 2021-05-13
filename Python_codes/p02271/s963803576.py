def solve():
    def dfs(idx, end, value, is_make):
        if idx == end:
            if value > 2000:
                return
            
            is_make[value] = True
            return

        dfs(idx + 1, end, value + A[idx], is_make)
        dfs(idx + 1, end, value, is_make)

    n = int(input())
    A = [int(i) for i in input().split()]
    q = int(input())
    M = [int(i) for i in input().split()]

    is_make = [False] * (2000 + 1)
    dfs(0, n, 0, is_make)

    for m in M:
        print('yes' if is_make[m] else 'no')

if __name__ == '__main__':
    solve()