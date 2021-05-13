def main():
    N = int(input())
    A = [int(a) for a in input().split()]

    idx = 0
    ans = 0
    for i in range(len(A)):
        if idx + 1 > len(A) - 1 :
            break

        m = ""
        if A[idx] < A[idx + 1]:
            m = "+"
        elif A[idx] > A[idx + 1]:
            m = "-"
        else:
            find = False
            for j in range(idx, len(A)-1):
                if A[j] < A[j + 1]:
                    m = "+"
                    find = True
                    idx = j
                    break
                elif A[j] > A[j + 1]:
                    m = "-"
                    find = True
                    idx = j
                    break
            if find == False:
                print(ans + 1)
                exit()

        for j in range(idx, len(A) - 1):
            if m == "+":
                if A[j] <= A[j + 1]:
                    idx = j + 1
                else:
                    idx = j + 1
                    ans += 1
                    break
            elif m == "-":
                if A[j] >= A[j + 1]:
                    idx = j + 1
                else:
                    idx = j + 1
                    ans += 1
                    break

    print(ans + 1)

if __name__ == "__main__":
    main()