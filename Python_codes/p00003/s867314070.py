def main():
    n = int(input())
    for i in range(n):
        a=[int(x) for x in input().split()]
        a.sort()
        if a[0] ** 2 + a[1] ** 2 != a[2] ** 2:
            print("NO")
        else:
            print("YES")

main()
