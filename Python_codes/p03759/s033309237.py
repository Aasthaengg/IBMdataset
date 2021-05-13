def solve():
    A, B, C = map(int, input().split())

    if B - A == C - B:
        return True

    return False


if __name__ == '__main__':
    res = solve()
    if res:
        print("YES")
    else:
        print("NO")
