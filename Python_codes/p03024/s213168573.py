def solve():
    s = input()
    k = len(s)
    if s.count("o")+(15-k) >= 8:
        print("YES")
    else:
        print("NO")
    return 0

if __name__ == "__main__":
    solve()
