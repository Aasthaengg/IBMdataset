
def main():
    a = list(map(int, input().split()))
    sorted_a = sorted(a)
    print(int(str(sorted_a[2]) + str(sorted_a[1])) + sorted_a[0])


if __name__ == "__main__":
    main()
