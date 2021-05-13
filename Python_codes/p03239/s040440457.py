def main():
    n,t=map(int,input().split())
    ct=[tuple(map(int,input().split())) for _ in range(n)]
    minc = 1001
    for c,tt in ct:
        if t >= tt and minc > c:
            minc = c
    print(minc if minc != 1001 else "TLE")

if __name__ == "__main__":
    main()