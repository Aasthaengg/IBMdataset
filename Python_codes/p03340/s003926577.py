def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    right = 0
    left = 0
    cnt = 0
    
    total = 0
    for left in range(0, N):
        
        while (right < N and total ^ A[right] == total+A[right]):
            total += A[right]
            right += 1
        
        cnt += right - left
        if right == left:
            right += 1
        else:
            total -= A[left]
    print(cnt)


if '__main__' == __name__:
    resolve()