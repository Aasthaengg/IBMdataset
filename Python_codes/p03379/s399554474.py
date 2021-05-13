def main():
    n = int(input())
    inlis = list(map(int, input().split()))
    inlis_sort = sorted(inlis)

    low = inlis_sort[int(n/2)-1]
    high = inlis_sort[int(n/2)]
    ave = (low + high) / 2

    for i in inlis:
        if i >= ave:
            print(low)
        else:
            print(high)

    
    

if __name__ == "__main__":
    main()
