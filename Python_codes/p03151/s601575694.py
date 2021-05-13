def solve(N, A, B):
    if sum(A) < sum(B):
        print(-1)
        return

    diff = [a - b for a, b in zip(A, B)]
    changed = [False for _ in range(N)]
    diff.sort()
    l, r = 0, N - 1

    while diff[l] < 0:
        if diff[l] + diff[r] >= 0:
            changed[l] = True
            changed[r] = True
            diff[r] += diff[l]
            l += 1
        else:
            changed[l] = True
            changed[r] = True
            diff[l] += diff[r]
            r -= 1
    print(sum(changed))
    return


if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split(' ')))
    B = list(map(int, input().split(' ')))

    solve(N, A, B)