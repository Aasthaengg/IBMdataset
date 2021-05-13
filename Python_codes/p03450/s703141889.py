import sys
import collections

input = sys.stdin.readline


def main():
    N, M = [int(x) for x in input().split()]
    LRD = [[int(x) for x in input().split()] for _ in range(M)]
    A = [[] for j in range(N + 1)]

    if M == 0:
        print("Yes")
        return

    slist = set()
    for l, r, d in LRD:
        A[l].append([r, d])
        A[r].append([l, -d])
        slist.add(l)
        slist.add(r)

    dmemo = [None] * (N + 1)

    f = False
    for i in list(slist):
        if dmemo[i] is not None:
            continue
        s = collections.deque()
        s.append(i)
        dmemo[i] = 0

        while s:
            c = s.pop()
            for r, d in A[c]:
                if dmemo[r] is not None:
                    if dmemo[r] - dmemo[c] != d:
                        f = True
                        break
                else:
                    dmemo[r] = dmemo[c] + d
                    s.append(r)
            if f:
                break
        if f:
            break

    if f:
        print("No")
    else:
        print("Yes")


if __name__ == '__main__':
    main()
