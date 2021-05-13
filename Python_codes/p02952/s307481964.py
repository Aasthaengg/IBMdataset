def solve():
    N = int(input())
    count = 0
    for i in range(N):
        if(int(len(str(i+1))) % 2 == 1):
            count += 1
    print(count)


if __name__ == "__main__":
    solve()