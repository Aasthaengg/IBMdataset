def main():
    N = int(input())
    v = [int(a) for a in input().split()]
    c = [int(a) for a in input().split()]
    ds = 0
    for i in range(N):
        d = v[i] - c[i]
        if d > 0:
            ds += d
    print(ds)
main()