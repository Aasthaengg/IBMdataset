
def main():

    N = int(input())
    A = input()
    B = input()
    C = input()

    count = 0
    for i in range(N):
        if A[i] == B[i] == C[i]:
            pass
        elif A[i] == B[i]:
            count += 1
        elif A[i] == C[i]:
            count += 1
        elif B[i] == C[i]:
            count += 1
        else:
            count += 2
    return count

if __name__ == '__main__':
    print(main())