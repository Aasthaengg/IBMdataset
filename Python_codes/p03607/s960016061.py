def c(s):
    n = input()
    if n in s:
        s.remove(n)
    else:
        s.add(n)

def main():
    n = int(input())
    s = set()

    for i in range(n):
        c(s)

    print(len(s))


if __name__ == '__main__':
    main()
