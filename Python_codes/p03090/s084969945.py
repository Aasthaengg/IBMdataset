# AGC032B - Balanced Neighbors
def main():
    N = int(input())
    if N % 2:
        V = [(i, N - i) for i in range(1, N // 2 + 1)]  # pairs of vertices
        V += [(N,)]
    else:
        V = [(i, N - i + 1) for i in range(1, N // 2 + 1)]
    E, l = [], len(V)  # edges
    for i in range(l - 1):
        E += [(v, u) for v in V[i] for u in V[i + 1]]
    if l >= 3:
        E += [(v, u) for v in V[0] for u in V[-1]]
    print(len(E))
    print("\n".join(["{} {}".format(v, u) for v, u in E]))


if __name__ == "__main__":
    main()