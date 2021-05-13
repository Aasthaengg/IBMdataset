def main():
    n = int(input())
    ans = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if i == j or i + j == n + (n + 1) % 2:
                continue
            ans.append([i, j])
    print(len(ans))
    for a in ans:
        print(" ".join(map(str, a)))


if __name__ == '__main__':
    main()
