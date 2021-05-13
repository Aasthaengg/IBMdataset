def solve():
    w = list(input())
    s = set(w)
    for i in s:
        if len([x for x in w if x == i]) % 2 == 1:
            print('No')
            exit()
    print('Yes')

if __name__ == "__main__":
    solve()