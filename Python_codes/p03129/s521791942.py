def main():
    N, K = (int(i) for i in input().split())
    if (N+1)//2 >= K:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
