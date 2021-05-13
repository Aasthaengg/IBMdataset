from itertools import accumulate


def main():
    number, operations = [int(x) for x in input().split()]
    dists = [int(x) for x in input().split()]

    for _ in range(operations):
        temp = [0] * (number + 1)
        for i, v in enumerate(dists):
            left = max(i - v, 0)
            right = min(i + v + 1, number)
            temp[left] += 1
            temp[right] -= 1
        templi = list(accumulate(temp))
        if templi == dists:
            break
        else:
            dists = templi
    dists.pop()
    print(*dists)


if __name__ == '__main__':
    main()

# Pypy 3 なら通る。Python 3 では無理。
