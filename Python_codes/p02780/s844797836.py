
from itertools import accumulate
def resolve():
    def ev(x):
        return (x*(x+1)//2)/x

    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    E = [0]+[ev(a) for a in A]
    E = list(accumulate(E))
    ans = 0
    for i in range(N-K+1):
        if ans < E[i+K] - E[i]:
            ans = E[i + K] - E[i]
    print(ans)

if __name__ == "__main__":
    resolve()