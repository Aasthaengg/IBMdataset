def kaibu(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

def solve():
    a, b = map(int, input().split())
    ans = 0
    for i in range(a, b+1):
        if kaibu(i) == True:
            ans += 1
    print(ans)
    return 0

if __name__ == "__main__":
    solve()
