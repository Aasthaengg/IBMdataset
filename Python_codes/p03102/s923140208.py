def main():
    N, M, C = map(int, input().split())
    B = list(map(int, input().split()))
    cnt = 0
    calc = 0

    for i in range(N):
        calc = 0
        A = list(map(int, input().split()))
        for j in range(len(A)):
            calc += A[j] * B[j]
        if calc + C > 0:
            cnt += 1
    print(cnt)
main()