def resolve():
    N = int(input())
    P = list(map(int, input().split()))
    expected = []
    real = []
    for i in range(1, N+1):
        if i == P[i-1]:
            continue
        expected.append(i)
        real.append(P[i-1])
    print("YES" if len(real) == 0 or (len(real)==2 and len(expected)==2 and expected[0]==real[1] and expected[1]==real[0]) else "NO")

if '__main__' == __name__:
    resolve()