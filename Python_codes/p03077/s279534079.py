import math
def main():
    N = int(input())
    A = int(input())
    B = int(input())
    C = int(input())
    D = int(input())
    E = int(input())
    cost = [A, B, C, D, E]

    f = lambda x : int((N//x))
    t = [f(A), f(B), f(C), f(D), f(E)]

    idx = 0
    ma = 0

    for i in range(len(t)):
        if t[i] > ma:
            ma = t[i]
            idx = i
    ma += idx

    ans = ma + (5 - idx)

    if N % cost[idx] == 0:
        ans -= 1

    print(ans)

if __name__ == "__main__":
    main()