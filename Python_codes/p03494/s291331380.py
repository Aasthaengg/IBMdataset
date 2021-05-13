def main():
    N = int(input())
    A = list(map(int, input().split()))
    cnt = 0
    flag = 0

    while flag == 0:
        for i in range(N):
            if A[i] % 2 != 1:
                A[i] = A[i] // 2
            else:
                flag = 1
                print(cnt)
                return
        cnt += 1

main()