def main():
    n = int(input())
    blis = list(map(int, input().split()))

    alis = [blis[0], blis[0]]
    if n > 2 and alis[1] > blis[1]:
        alis[1] = blis[1]
    if n > 2:
        for i in range(3, n):
            alis.append(min(blis[i-2], blis[i-1]))
    if n > 2:
        alis.append(blis[n-2])
    print(sum(alis))


    


if __name__ == "__main__":
    main()
