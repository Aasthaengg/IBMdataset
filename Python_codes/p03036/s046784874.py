def main():
    r, D, x = map(int, input().split())
    ans = []
    for _ in range(10):
        x = r * x - D
        ans.append(str(x))
    print("\n".join(ans))


if __name__ == '__main__':
    main()
