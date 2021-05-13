def main():
    N = int(input())
    ans = [0]*(N+1)
    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                a = x*x + y*y + z*z + x*y + y*z + z*x
                if a <= N:
                    ans[a] += 1
    for i in range(1, N+1):
        print(ans[i])


if __name__ == "__main__":
    main()
