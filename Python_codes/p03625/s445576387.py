def main():
    n = int(input())
    As = sorted(list(map(int, input().split())))
    edeges = []
    i = 0
    while i < n-1:
        if As[i] == As[i+1]:
            edeges.append(As[i])
            i += 1
        i += 1
    if len(edeges) < 2:
        ans = 0
    else:
        ans = edeges[-1] * edeges[-2]
    print(ans)


if __name__ == "__main__":
    main()
