h, w = map(int, input().split())
A = [["#"]*(w+2)] + [["#"] + [s for s in input()] + ["#"]
                     for _ in range(h)] + [["#"]*(w+2)]


def main():
    step = 0
    Q = set([])
    for hh in range(1, h + 1):
        for ww in range(1, w + 1):
            if A[hh][ww] == "#":
                if A[hh - 1][ww] == ".":
                    Q.add((hh - 1, ww))
                if A[hh][ww - 1] == ".":
                    Q.add((hh, ww - 1))
                if A[hh + 1][ww] == ".":
                    Q.add((hh + 1, ww))
                if A[hh][ww + 1] == ".":
                    Q.add((hh, ww + 1))
    while len(Q) > 0:
        step += 1
        new = set([])
        for hh, ww in Q:
            A[hh][ww] = "#"
        while len(Q) > 0:
            hh, ww = Q.pop()
            if A[hh - 1][ww] == ".":
                A[hh-1][ww] = "#"
                new.add((hh - 1, ww))
            if A[hh][ww - 1] == ".":
                A[hh][ww-1] = "#"
                new.add((hh, ww - 1))
            if A[hh + 1][ww] == ".":
                A[hh+1][ww] = "#"
                new.add((hh + 1, ww))
            if A[hh][ww + 1] == ".":
                A[hh][ww + 1] = "#"
                new.add((hh, ww + 1))
        Q = new.copy()
    print(step)
    return


if __name__ == "__main__":
    main()
