import itertools

def main():
    N = int(input())
    P = input().replace(" ", "")
    Q = input().replace(" ", "")
    vals = []
    for comb in itertools.permutations(list(map(str, range(1, N+1))), N):
        vals.append("".join(comb))
    vals.sort()
    print(abs(vals.index(P) - vals.index(Q)))


if __name__ == '__main__':
    main()
