def solve():
    N = input()
    a = ['']
    for i in input().split():
        a.insert(int(i)-1, i)
    print(*a[-1]and[-1]or a)

solve()