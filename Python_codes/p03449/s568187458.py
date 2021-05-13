def main():
    n = int(input())
    A1 = list(map(int, input().split()))
    A2 = list(map(int, input().split()))
    ans = 0

    for i in range(n - 1):
        A1[i + 1] += A1[i]
        A2[n - i - 2] += A2[n - i - 1]
        
    for i in range(n):
        ans = max(ans, A1[i] + A2[i])
    
    print(ans)


if __name__ == '__main__':
    main()