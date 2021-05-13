def main():
    n = int(input())
    vlis = list(map(int, input().split()))
    clis = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        value = vlis[i] - clis[i]
        if value > 0:
            ans += value
    print(ans)

if __name__ == "__main__":
    main()
