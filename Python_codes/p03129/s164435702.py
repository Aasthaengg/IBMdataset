# yahoo-procon2019-qualA - Anti-Adjacency
def main():
    n, k = list(map(int, input().rstrip().split()))
    print("YES" if (n + 1) // 2 >= k else "NO")


if __name__ == "__main__":
    main()