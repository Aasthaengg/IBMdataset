def main():
    N = int(input())
    jobs = []
    time = 0
    for _ in range(N):
        A, B = map(int, input().split())
        jobs.append((A, B))

    jobs = sorted(jobs, key=lambda x: x[1])
    for j in jobs:
        time += j[0]
        if time > j[1]:
            print("No")
            return
        
    else:
        print("Yes")


if __name__ == '__main__':
    main()