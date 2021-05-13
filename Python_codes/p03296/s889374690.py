def resolve():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, n):
        if a[i] == a[i - 1]:
            ans += 1
            a[i] = -1
    print(ans)
            

if __name__ == "__main__":
    resolve()
