def main():

    N = int(input())
    T = list(map(int, input().split()))
    A = list(map(int, input().split()))
    mod = pow(10, 9) + 7

    heightT = []
    for i in range(N):
        if i == 0:
            heightT.append([T[i], "exact"])
        else:
            if T[i] > T[i-1]:
                heightT.append([T[i], "exact"])
            elif T[i] == T[i-1]:
                heightT.append([T[i], "bound"])
            else:
                return 0
    heightA = []
    for i in range(N-1, -1, -1):
        if i == N-1:
            heightA.append([A[i], "exact"])
        else:
            if A[i+1] < A[i]:
                heightA.append([A[i], "exact"])
            elif A[i+1] == A[i]:
                heightA.append([A[i], "bound"])
            else:
                return 0
    heightA = heightA[::-1]

    ans = 1
    for i in range(N):
        if heightT[i][1] == "exact" and heightA[i][1] == "exact":
            if heightT[i][0] != heightA[i][0]:
                return 0
        elif heightT[i][1] == "exact" and heightA[i][1] == "bound":
            if heightT[i][0] > heightA[i][0]:
                return 0
        elif heightT[i][1] == "bound" and heightA[i][1] == "exact":
            if heightT[i][0] < heightA[i][0]:
                return 0
        else:
            ans *= min(heightT[i][0], heightA[i][0])
            ans %= mod
    return ans


if __name__ == '__main__':
    print(main())