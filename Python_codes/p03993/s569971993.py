def main():
    N = int(input())
    A = [int(x)-1 for x in input().split()]
    ans = 0
    for i in range(N):
        if i==A[A[i]]:
            ans += 1
    print(ans//2)
if __name__ == '__main__':
    main()