def main():
    a, b, c = [int(x) for x in input().split()]
    times = b // a
    if times < c:
        print(times)
    else:
        print(c)
main()
