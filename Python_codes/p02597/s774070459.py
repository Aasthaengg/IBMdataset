def solve():
    N = int(input())
    C = list(input())

    right = N-1
    left = 0

    cnt = 0
    while left < right:
        while left < N and C[left] == 'R':
            left += 1

        while right >= 0 and C[right] == 'W':
            right -= 1
        
        if left >= right:
            break
        
        C[left], C[right] = C[right], C[left]
        cnt += 1
    
    print(min(cnt,C.count("R"), C.count("W")))
    
if __name__ == '__main__':
    solve()