def main():
    n = int(input())
    hlis = list(map(int, input().split()))
    ans = 0
    tmp = 0
    for i in range(n-1):      
        if hlis[i+1] <= hlis[i]:
            tmp += 1
        else:
            if ans < tmp:
                ans = tmp
            tmp = 0
    if ans < tmp:
        ans = tmp
    print(ans)
    


if __name__ == "__main__":
    main()
