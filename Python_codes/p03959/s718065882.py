N = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
R = []
M = 1000000007


def main():
    global R
    global A
    p = -1
    for t in T:
        if t > p: # new
            R.append(t)
            p = t
        else:
            R.append(-t)

    # reverse direction
    R = list(reversed(R))
    A = list(reversed(A))

    p = -1
    for i, t in enumerate(A):
        r = R[i]
        if r < 0:
            max_h = -r
            if t > p: # new
                p = t
                if t <= max_h:
                    R[i] = t
                else:
                    return 0
            else:
                R[i] = -min(max_h, t)
        else:
            if t > p: # new
                p = t
                if t != r:
                    return 0
            else:
                if r > t:
                    return 0

    answer = 1
    for r in R:
        if r > 0:
            answer *= 1
        else:
            max_h = -r
            answer *= max_h
            answer %= M
    return answer
print(main())
