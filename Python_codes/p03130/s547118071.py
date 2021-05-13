# yahoo-procon2019-qualB - Path
def main():
    C = [0] * 4
    for _ in range(3):
        a, b = list(map(int, input().rstrip().split()))
        C[a - 1] += 1
        C[b - 1] += 1
    print("YES" if set(C) == {1, 2} else "NO")


if __name__ == "__main__":
    main()