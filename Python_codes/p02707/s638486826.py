def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    Subs = [0 for _ in range(N)]
    for i, a in enumerate(A):
        Subs[a-1] += 1
    [print(n) for n in Subs]

if '__main__' == __name__:
    resolve()