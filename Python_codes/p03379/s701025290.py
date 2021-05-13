def main():
    n = int(input())
    xs = list(map(int, input().split()))
    xs_sorted = sorted(xs)
    mid_n2, mid_n1 = (n+1)//2, (n-1)//2
    for x in xs:
        if x == xs_sorted[mid_n1]:
            print(xs_sorted[mid_n2])
        elif x == xs_sorted[mid_n2]:
            print(xs_sorted[mid_n1])
        elif x < xs_sorted[mid_n1]:
            print(xs_sorted[mid_n2])
        else:
            print(xs_sorted[mid_n1])


if __name__ == "__main__":
    main()
