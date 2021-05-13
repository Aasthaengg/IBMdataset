def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    T = {0: 1}
    t = 0
    r = 0
    for i in range(len(A)):
        t = (t + A[i]) % M
        r += T.get(t, 0)
        T[t] = T.get(t, 0) + 1
    print(r)
main()
