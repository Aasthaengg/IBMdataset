def main():
    n = int(input())
    a = [int(input()) for _ in range(n)]
    a_copy = sorted(a)
    a_max = a_copy[-1]
    a_second = a_copy[-2]
    for i in range(n):
        if a[i] == a_max:
            print(a_second)
        else:
            print(a_max)


main()