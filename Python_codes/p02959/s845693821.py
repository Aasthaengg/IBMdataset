def main():
    n = int(input())
    alis = list(map(int, input().split()))
    blis = list(map(int, input().split()))
    ans = 0

    for i in range(n-1, -1, -1):
        if blis[i] <= alis[i+1]:
            ans += blis[i]
        elif blis[i] < alis[i+1] + alis[i]:
            ans += blis[i]
            alis[i] = alis[i] - (blis[i] - alis[i+1]) 
        elif blis[i] >= alis[i+1] + alis[i]:
            ans += alis[i] + alis[i+1]
            alis[i] = 0
    print(ans)


if __name__ == "__main__":
    main()
