def main():
    n, k = map(int, input().split())
    if (n-1)*(n-2)//2 < k:
        print("-1")
    else:
        ans = []
        buf = (n-1)*(n-2)//2
        for i in range(2, n+1):
            ans.append([1, i])
        for i in range(2, n):
            if buf == k:
                break
            for j in range(i+1, n+1):
                ans.append([i, j])
                buf -= 1
                if buf == k:
                    break
        print(len(ans))
        for v in ans:
            print(v[0], v[1])

if __name__ == "__main__":
    main()