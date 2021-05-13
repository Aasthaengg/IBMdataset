def main():
    n = int(input())
    b = list(map(int, input().split()))
    ans = []
    f = True
    for i in reversed(range(n)):
        F = True
        for j in reversed(range(i+1)):
            if b[j] == j+1:
                ans.append(b.pop(j))
                F = False
                break
        if F:
            f = False
            break
    if f:
        for v in reversed(ans):
            print(v)
    else:
        print(-1)

if __name__ == "__main__":
    main()
