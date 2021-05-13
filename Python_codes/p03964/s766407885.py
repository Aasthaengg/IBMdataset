import math
def resolve():
    N = int(input())
    TA = [list(map(int, input().split())) for i in range(N)]
    t, a = TA[0]
    for i in range(1, len(TA)):
        t_next, a_next = TA[i]
        div = max((t//t_next)+(t%t_next!=0), (a//a_next)+(a%a_next!=0))
        t = t_next*div
        a = a_next*div
    print(t+a)


if '__main__' == __name__:
    resolve()

