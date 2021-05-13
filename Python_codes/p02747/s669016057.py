def solve():
    s = input()
    for i in range(1,6):
        if s == "hi"*i:
            print("Yes")
            exit()
    print("No")
    return 0

if __name__ == "__main__":
    solve()