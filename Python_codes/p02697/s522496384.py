def main():
    N, M =map(int, input().split())

    if N % 2:
        left = 1
        right = N - 1
        for _ in range(M):
            print(left, right)
            left += 1
            right -= 1
    else:
        left = 1
        right = N - 1
        flag = False
        for _ in range(M):
            if right - left <= N//2:
                flag = True
            
            if flag:
                print(left, right-1)
            else:
                print(left, right)
            
            left += 1
            right -= 1

        
if __name__ == "__main__":
    main()