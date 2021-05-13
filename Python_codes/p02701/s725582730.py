def main():
    N = int(input())
    counter = set()
    for i in range(N):
        s = input()
        counter.add(s)
    print(len(counter))


main()
