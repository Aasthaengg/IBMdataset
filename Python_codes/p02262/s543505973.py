def insertion(A, n, g):
    global cnt
    for i in range(g, n):
        while i >= g and A[i - g] > A[i]:
            A[i], A[i - g] = A[i - g], A[i]
            i -= g
            cnt += 1

def main():
    global cnt
    cnt = 0
    n = int(raw_input())
    A = [int(raw_input()) for i in range(n)]

    G = list()
    h = 1
    k = 1
    while h <= n:
        G.append(h)
        h = (4 ** k) + (3 * (2 ** (k - 1)) + 1)
        k += 1
    G = G[::-1]

    for i in G:
        insertion(A, n, i)

    print(len(G))
    print(" ".join(map(str, G)))
    print(cnt)
    for j in A: print(j)

main()