def main():
    import sys
    N = int(input())
    A = ["?"]*N
    pos = N//2
    left = 0
    right = N
    if A[left] == "?":
        print(left)
        sys.stdout.flush()
        S = input()[0]
        if S == "V":
            return
        A[left] = S
    for i in range(20):
        pos = (left+right)//2
        if A[pos] == "?":
            print(pos)
            sys.stdout.flush()
            S = input()[0]
            if S == "V":
                return
            A[pos] = S

        if (pos - left) % 2 == 0:
            if A[pos] == A[left]:
                left = pos
            else:
                right = pos
        else:
            if A[pos] != A[left]:
                left = pos
            else:
                right = pos


if __name__ == '__main__':
    main()
