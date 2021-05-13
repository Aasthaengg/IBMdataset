def resolve():
    n = int(input())
    C = [0, 0]
    S = list(map(int, input().split()))
    for i in range(2):
        tmp = 0
        for j in range(n):
            tmp += S[j]
            if (i+j)%2==0:
                if tmp <= 0:
                    C[i] += abs(tmp) + 1
                    tmp = 1
            else:
                if tmp >= 0:
                    C[i] += abs(tmp) + 1
                    tmp = -1

    print(min(C[0], C[1]))

if __name__ == '__main__':
    resolve()