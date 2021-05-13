def main():
    N = int(input())
    ans = [0 for i in range(N + 1)]

    for x in range(1, 101):
        for y in range(1, 101):
            for z in range(1, 101):
                s = x**2 + y**2 + z**2 + x*y + y*z + z*x

                if 1 <= s <= N:
                    ans[s] += 1

    for i in range(1, N + 1):
        print(ans[i])

if __name__ == "__main__":
    main()