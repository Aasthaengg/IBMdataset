
def main():
    n = int(input())
    p = list(map(int, input().split(" ")))
    ans = 0
    min = 2e5+1
    for i in range(n):
        if min > p[i]:
            min = p[i]
        if p[i] <= min:
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()