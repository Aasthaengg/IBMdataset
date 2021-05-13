def main():
    N = int(input())
    A = list(map(int, input().split()))
    end = len(A)
    judge = 0
    ans = 0
    i = 0

    if end == 1:
        return 1

    while True:
        if A[i] < A[i+1]:
            ans += 1
            while True:
                i += 1
                if i == end-1:
                    return ans
                elif A[i] <= A[i+1]:
                    continue
                else:
                    i += 1
                    if i == end-1:
                        ans += 1
                        return ans
                    else:
                        break

        elif A[i] > A[i+1]:
            ans += 1
            while True:
                i = i+1
                if i == end-1:
                    return ans
                elif A[i] >= A[i+1]:
                    continue
                else:
                    i += 1
                    if i == end-1:
                        ans += 1
                        return ans
                    else:
                        break

        elif A[i] == A[i+1]:
            i += 1
            if i == end-1:
                ans += 1
                return ans
            else:
                continue

print(main())
