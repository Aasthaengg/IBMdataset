def solve():
    N = int(input())
    A = [int(x) for x in input().split()]
    right = 0
    sum = 0
    res = 0
    for left in range(N):
        while right < N and (right <= left or sum^A[right] == sum + A[right]):
            sum += A[right]
            right += 1
        res += (right - left)
        if right == left: right += 1
        else:
            sum -= A[left]
    return res

if __name__ == '__main__':
    print(solve())
