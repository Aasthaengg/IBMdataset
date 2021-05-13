def main():
    n = int(input())
    i = 1
    now = n
    while True:
        if now % 360 == 0:
            print(i)
            break
        else:
            i += 1
            now += n


main()
