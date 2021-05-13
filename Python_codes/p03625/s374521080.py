import collections

def main():
    N = input()
    A = map(int, input().split())
    c = collections.Counter(A)
    edge1 = None
    for edge, freq in sorted(c.items(), key=lambda x: -x[0]):
        if edge1 is None and freq >= 4:
            print(edge ** 2)
            exit()
        elif edge1 is None and freq >= 2:
            edge1 = edge
        elif edge1 is not None and freq >= 2:
            print(edge1 * edge)
            exit()
    print(0)


if __name__ == '__main__':
    main()
