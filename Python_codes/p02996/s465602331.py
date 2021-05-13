if __name__ == "__main__":
    N = int(input())
    tasks = []
    for _ in range(N):
        a, b = map(int, input().split())
        tasks.append((b, a))
    tasks.sort()
    t = 0
    for b, a in tasks:
        if t + a > b:
            break
        t += a
    else:
        print("Yes")
        exit(0)
    print("No")
