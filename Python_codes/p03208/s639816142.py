def main():
    n, k = map(int, input().split())
    inlis = list()
    for _ in range(n):
        h = int(input())
        inlis.append(h)
    inlis.sort()
    ans = 10 ** 10
    for i in range(n-k+1):
        tmp = inlis[i+k-1] - inlis[i]
        if tmp < ans:
            ans = tmp
    print(ans)
            



if __name__ == "__main__":
    main()