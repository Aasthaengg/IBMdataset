import sys

readline = sys.stdin.readline

flagset = ['not increase', 'flat', 'not decrease']

def main():
    N = int(readline())
    A = list(map(int, readline().split()))

    cnt = 0
    A0 = A[0]
    flag = flagset[1]
    for i in range(N-1):
        Ai = A[i]
        Ai1 = A[i+1]
        if flag == 'flat':
            if Ai < Ai1:
                flag = 'not decrease'
            elif Ai > Ai1:
                flag = 'not increase'
            elif Ai == Ai1:
                flag = 'flat'
            else:
                cnt += 1
        elif flag == 'not decrease':
            if Ai <= Ai1:
                continue
            else:
                flag = 'flat'
                cnt += 1
        else:
            if Ai >= Ai1:
                continue
            else:
                flag = 'flat'
                cnt += 1
    cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
