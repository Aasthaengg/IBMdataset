if __name__ == "__main__":
    a, b = map(int, input().split())
    if (a+b) % 2 == 1:
        ans = 1
    else:
        ans = 0
    ans += (a + b) // 2
    print(ans)
