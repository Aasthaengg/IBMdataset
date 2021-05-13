def solve():
    n = int(input())
    s = input()
    tmp = 0
    for i in range(n - 2):
        if (s[i], s[i+1], s[i+2]) == ("A", "B", "C"):
            tmp += 1
    print(tmp)
solve()
