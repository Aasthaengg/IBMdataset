def main():
    N = int(input())
    A = input()
    B = input()
    C = input()
    cnt = 0

    for i in range(N):
        if A[i] == B[i] == C[i]:
            continue
        else:
            if A[i] == B[i] or A[i] == C[i] or B[i] == C[i]:
                cnt += 1
            else:
                cnt += 2

    print(cnt)


main()
