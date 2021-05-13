def main():
    N = int(input())
    task = [list(map(int, input().split())) for i in range(N)]
    task.sort(key = lambda x : x[1])
    time = 0

    for t in task:
        if time + t[0] <= t[1]:
            time += t[0]
        else:
            print("No")
            exit()

    print("Yes")

if __name__ == "__main__":
    main()