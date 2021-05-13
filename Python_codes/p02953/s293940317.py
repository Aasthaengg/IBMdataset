def main():
    n = int(input())
    hlis = list(map(int, input().split()))

    for i in range(0, n-1):
        if hlis[i]-1 > hlis[i+1]:
            print("No")
            exit()
        elif hlis[i]-1 == hlis[i+1]:
            hlis[i] = hlis[i] - 1
            if i > 1 and hlis[i-1] > hlis[i]:
                print('No')
                exit()
        elif i > 1 and hlis[i-1] <= hlis[i] - 1:
            hlis[i] = hlis[i]-1
    print("Yes")

if __name__ == "__main__":
    main()
