def solve():
    a, b, k = map(int, input().split())
    ans = list()
    for i in range(a, min(a+k, b+1), 1):
        ans.append(i)
    for i in range(b, max(b-k,a), -1):
        ans.append(i)
    ans = list(set(ans))
    ans.sort()
    for i in ans:
        print(i)
    return 0

if __name__ == "__main__":
    solve()
