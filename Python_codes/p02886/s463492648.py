def main():
    n = int(input())
    d = [int(x) for x in input().split()]
    ans = 0
    for i in range(n):
        for j in range(n):
            if i < j:
                ans += d[i]*d[j]
    print(ans)

if __name__ == '__main__':
    main()