def main():
    n = int(input())
    if n % 2 == 0:
        ans = []
        for i in range(1, n//2):
            ans.append([i, i+1])
            ans.append([i, n-i])
            ans.append([n-i+1, i+1])
            ans.append([n-i+1, n-i])
        if n >= 6:
            ans.append([1, n//2])
            ans.append([1, n//2+1])
            ans.append([n, n//2])
            ans.append([n, n//2+1])
        print(len(ans))
        for p, q in ans:
            print(p, q)
    else:
        ans = []
        n -= 1
        for i in range(1, n//2):
            ans.append([i, i+1])
            ans.append([i, n-i])
            ans.append([n-i+1, i+1])
            ans.append([n-i+1, n-i])
        ans.append([1, n+1])
        ans.append([n, n+1])
        if n >= 4:
            ans.append([n//2, n+1])
            ans.append([n//2+1, n+1])
        print(len(ans))
        for p, q in ans:
            print(p, q)

if __name__ == "__main__":
    main()