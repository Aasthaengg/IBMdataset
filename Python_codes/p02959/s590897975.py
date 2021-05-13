def main():
    n = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))

    ans = 0
    for i in range(n-1, -1, -1):
        if Bs[i] >= As[i+1]:
            Bs[i] -= As[i+1]
            ans += As[i+1]
            As[i+1] = 0
        else:
            As[i+1] -= Bs[i] 
            ans += Bs[i]
            Bs[i] = 0

        if Bs[i] >= As[i]:
            Bs[i] -= As[i]
            ans += As[i]
            As[i] = 0
        else:
            As[i] -= Bs[i]
            ans += Bs[i]
            Bs[i] = 0
    print(ans)


if __name__ == "__main__":
    main()
