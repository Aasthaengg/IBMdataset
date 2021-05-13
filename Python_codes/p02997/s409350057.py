def main():
    n, k = map(int, input().split())
    lim = (n-2)*(n-1)//2
    if lim < k:
        print(-1)
    else:
        ans = []
        for i in range(2, n+1):
            ans.append([1, i])
        x = lim
        for i in range(2, n):
            for j in range(i+1, n+1):
                if x == k:
                    break
                ans.append([i, j])
                x -= 1
            if x == k:
                break
        print(len(ans))
        for u, v in ans:
            print(u, v)

if __name__ == "__main__":
    main()