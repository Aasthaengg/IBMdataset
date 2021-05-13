def solve():
    ret = 1
    cur_num = X
    while cur_num * 2 <= Y:
        cur_num *= 2
        ret += 1
    print(ret)

if __name__ == "__main__":
    X, Y = map(int, input().split())
    solve()