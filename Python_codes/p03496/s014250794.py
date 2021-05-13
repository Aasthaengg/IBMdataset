def main():
    N = int(input())
    a = list(map(int, input().split()))

    amax = max(a)
    amax_arg = a.index(amax)
    amin = min(a)
    amin_arg = a.index(amin)

    output = []

    if abs(amax) >= abs(amin):
        for i in range(N):
            a[i] += amax
            output.append([amax_arg+1, i+1])
        for i in range(N-1):
            a[i+1] += a[i]
            output.append([i+1, i+2])
    else:
        for i in range(N):
            a[i] += amin
            output.append([amin_arg+1, i+1])
        for i in range(N-1):
            a[-i-2] += a[i-1]
            output.append([N-i, N-i-1])

    print(len(output))
    for i in range(len(output)):
        print(str(output[i][0])+" "+str(output[i][1]))


if __name__ == '__main__':
    main()

