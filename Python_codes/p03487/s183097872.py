from collections import Counter
def main():
    n = int(input())
    a = tuple(map(int, input().split()))
    ac = Counter(a)
    r = 0
    for ace in ac:
        if ac[ace] < ace:
            r += ac[ace]
        else:
            r += (ac[ace] - ace)
    print(r)

if __name__ == '__main__':
    main()
