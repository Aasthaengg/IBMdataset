def main():
    n, k = map(int, input().split())
    inlis = list()

    for _ in range(n):
        alis = list(map(int, input().split()))
        inlis.append(alis)
    inlis.sort()
    tmp = k
    i = 0

    while tmp > 0:
        tmp -= inlis[i][1]

        if tmp > 0:
            i += 1    
        else:
            print(inlis[i][0])
            exit()



if __name__ == "__main__":
    main()