def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    inlis = set(inlis)
    inlis = list(inlis)
    inlis.sort()

    while len(inlis) > 1:
        tmp = 0
        i = 1
        while tmp < len(inlis):
            #print(i, tmp)
            if inlis[i] % inlis[0] != 0:
                inlis[i] %= inlis[0]
                i += 1
                if i >= len(inlis):
                    break
            else:
                inlis.remove(inlis[i])
            tmp += 1
        inlis = set(inlis)
        inlis = list(inlis)
        inlis.sort()
        #print(inlis, len(inlis))
    print(inlis[0])


if __name__ == "__main__":
    main()