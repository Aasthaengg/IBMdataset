def main():
    n = int(input())
    a, b = list(map(int, input().split()))
    P = list(map(int, input().split()))
    ans = [[] for _ in range(3)]
    for p in P:
        if p <= a:
            ans[0].append(p)
        elif a + 1 <= p <= b:
            ans[1].append(p)
        else:
            ans[2].append(p)
    print(min(list(map(len, ans))))

if __name__ == '__main__':
    main()
