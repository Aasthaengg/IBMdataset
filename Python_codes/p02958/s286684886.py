def main():
    N = int(input())
    P = list(map(int, input().split()))
    diff = 0
    for p_org, p_sort in zip(P, sorted(P)):
        if p_org != p_sort:
            diff += 1
    if diff == 0 or diff == 2:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
