def abc174_e():
    n, k = map(int, input().split())
    A = list(map(int, input().split()))
    if k == 0: return max(A)

    lower, upper = 0, 10**9
    while upper - lower > 1:
        x = (upper + lower) // 2
        cnt = 0
        for a in A:
            cnt += a // x
            if a % x == 0: cnt -= 1
            if cnt > k: break
        if cnt > k: lower = x
        else: upper = x
    return upper

if __name__ == '__main__':
    print(abc174_e())