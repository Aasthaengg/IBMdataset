def main():
    K, X = map(int, input().split())
    ans = "Yes" if 500 * K >= X else "No"
    print(ans)



if __name__ == "__main__":
    main()
