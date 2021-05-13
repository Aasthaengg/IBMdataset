def main():
    n = int(input())
    x = 2
    while (x-1)*x//2 < n:
        x += 1
    if (x-1)*x//2 == n:
        print("Yes")
        ans = [[] for _ in range(x)]
        y = 1
        for i in range(x-1):
            for j in range(i+1, x):
                ans[i].append(y)
                ans[j].append(y)
                y += 1
        print(x)
        for i in range(x):
            print(len(ans[i]), end=" ")
            for j in range(len(ans[i])):
                print(ans[i][j], end="")
                if j < len(ans[i])-1:
                    print(" ", end="")
                else:
                    print("")
    else:
        print("No")

if __name__ == "__main__":
    main()
