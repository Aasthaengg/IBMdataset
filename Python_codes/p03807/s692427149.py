def solve():
    N = int(input())
    A = list(map(int, input().split()))

    if len([1 for x in A if x % 2 != 0]) % 2 != 0:
        return 'NO'
    else:
        return 'YES'

print(solve())