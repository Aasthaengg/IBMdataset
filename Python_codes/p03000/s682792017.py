def main():
    n, x = map(int, input().split())
    inlis = list(map(int, input().split()))
    ans = 1
    tmp = 0

    for i in range(n):
        tmp += inlis[i]
        if tmp <= x:
            ans += 1
        else:
            break
    print(ans)

    
if __name__ == "__main__":
    main()
