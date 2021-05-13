def solve():
    A,B,C = [int(i) for i in input().split()]
    set_nums = set([A,B,C])
    if len(set_nums) == 2:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    solve()