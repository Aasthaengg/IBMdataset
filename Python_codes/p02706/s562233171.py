def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split(' ')))
    homework_day = 0
    for i in range(len(A)):
        homework_day = homework_day + A[i]
    if homework_day > N:
        print(-1)
    else:
        print(N - homework_day)
main()