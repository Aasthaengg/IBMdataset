def solve():
    S= input()
    if len(S) != len(set(S)):
        print("no")
    else:
        print("yes")



if __name__ == '__main__':
    solve()