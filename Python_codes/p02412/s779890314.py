import itertools

def main():

    data = []
    while True:
        n, x = map(int, input().split())
        if [n, x] == [0, 0]: break
        data.append([n, x])

    for [n, x] in data:
        _list = list(range(1, n+1))
        comb = set(itertools.combinations(_list, 3))
        print(sum((True if sum(i) == x else False) for i in comb))


main()