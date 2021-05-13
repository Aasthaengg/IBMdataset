if __name__ == '__main__':
    n = int(input())
    b = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if (i + 1) < b[i]:
            print(-1)
            exit(0)
    for i in range(n):
        for j in range(len(b) - 1, -1, -1):
            if b[j] == (j + 1):
                ans.append(b[j])
                del b[j]
                break
        if len(b) != (n - i - 1):
            print(-1)
            exit(0)
    ans.reverse()
    for i in ans:
        print(i)