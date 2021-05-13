def main():
    N = int(input())
    b = list(map(int, input().split()))

    ans = []
    while b:
        for i in range(len(b) - 1, -1, -1):
            if i + 1 == b[i]:
                b.pop(i)
                ans.append(i + 1)
                break
        else:
            print(-1)
            return

    ans.reverse()
    for a in ans:
        print(a)


main()
