def main():
    N, a, b, c, d = (int(i) for i in input().split())
    S = input()
    if "##" in S[a:c] or "##" in S[b:d]:
        return print("No")
    if c < d:
        return print("Yes")
    # d < c
    if "..." in S[b-2:d+1]:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
