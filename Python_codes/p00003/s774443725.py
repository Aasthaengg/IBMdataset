for i in range(int(input())):
    li = sorted([int(j) for j in input().split()])
    print("YES" if li[0] ** 2 + li[1] ** 2 == li[2] ** 2 else "NO")