from bisect import bisect_left

def main():
    n, k = map(int, input().split())
    x = list(map(int, input().split()))

    zero_ind = bisect_left(x, 0)
    
    if zero_ind == 0:
        print(x[k-1])
        exit()
    elif zero_ind == n:
        print(-x[-k])
        exit()

    if x[zero_ind] == 0:
        x.pop(zero_ind)
        n -= 1
        k -= 1
    
    ans = float('inf')

    # only go to left
    if zero_ind >= k:
        ans = -x[zero_ind - k]

    # only go to right
    if n - zero_ind >= k and ans > x[zero_ind + k - 1]:
        ans = x[zero_ind + k - 1]

    # go to left and go to right
    for i in range(max(0, zero_ind - k + 1), zero_ind):
        if k+i-1 < n and ans > -2 * x[i] + x[k+i-1]:
            ans = -2 * x[i] + x[k+i-1]

    # go to right and go to left
    for i in range(zero_ind, min(n, zero_ind+k)):
        if 0 <= i-k+1 and ans > 2 * x[i] - x[i-k+1]:
            ans = 2 * x[i] - x[i-k+1]

    print(ans)

main()