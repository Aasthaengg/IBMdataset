def main():
    N, M = map(int, input().split())
    l = []
    for _ in range(N):
        x, y, z = map(int, input().split())
        l.append((x,y,z))
    r = 0
    l2 = [i+j+k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [i+j-k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [i-j+k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [i-j-k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [-i+j+k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [-i+j-k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [-i-j+k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    l2 = [-i-j-k for i, j, k in l]
    l2.sort(reverse=True)
    r = max(r, sum(l2[:M]))
    return r
print(main())
