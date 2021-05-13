def bubbleSort(n,A):
    flag = True
    cnt = 0
    while flag:
        flag = False
        for j in range(n-1, 0, -1):
            if A[j-1] > A[j]:
                A[j-1],A[j] = A[j],A[j-1]
                cnt += 1
                flag = True
    print(*A)
    print(cnt)

if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    bubbleSort(N, A)