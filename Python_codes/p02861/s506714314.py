
import sys, itertools


def solve(N: int, x: "List[int]", y: "List[int]"):
    route = list(itertools.permutations([i for i in range(N)]))
    length = 0
    itter = range(N-1)
    for i in route:
        for j in itter:
            length += ((x[i[j]]-x[i[j+1]])**2+(y[i[j]]-y[i[j+1]])**2)**0.5
    print(length/len(route))
    return
    
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    x = [int()] * (N)  # type: "List[int]"
    y = [int()] * (N)  # type: "List[int]"
    for i in range(N):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
    solve(N, x, y)

if __name__ == '__main__':
    main()
