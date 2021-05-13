import itertools

def main():
    n,w = [int(i) for i in input().split()]
    vals = [[], [], [], []]

    w0, v0 = [int(i) for i in input().split()]
    vals[0].append(v0)

    for i in range(n - 1):
        wi, vi = [int(i) for i in input().split()]
        vals[wi-w0].append(vi)

    vals[0].sort(reverse=True)
    vals[1].sort(reverse=True)
    vals[2].sort(reverse=True)
    vals[3].sort(reverse=True)

    ans = 0
    for i, j, k, l in itertools.product(range(len(vals[0])+1), range(len(vals[1])+1), range(len(vals[2])+1), range(len(vals[3])+1)):
        if i * w0 + j * (w0 + 1) + k * (w0 + 2) + l * (w0 + 3) <= w:
            ans = max(ans, sum(vals[0][:i]) + sum(vals[1][:j]) + sum(vals[2][:k]) + sum(vals[3][:l]))

    print(ans)

main()