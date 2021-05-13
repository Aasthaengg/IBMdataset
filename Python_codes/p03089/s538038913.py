def solve(remains, nums):
    if (len(remains)) == 0:
        [print(num) for num in nums[::-1]]
        exit()
    n_remain = None
    n_num = None
    for i, num in enumerate(remains):
        if i + 1 == num:
            n_remain = remains[:i] + remains[i + 1:]
            n_num = nums + [i + 1]
    if n_remain is None:
        return False
    solve(n_remain, n_num)


n = int(input())
B = [int(x) for x in input().split()]

solve(B, [])
print(-1)
