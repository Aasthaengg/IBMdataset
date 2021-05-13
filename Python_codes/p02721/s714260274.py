# kotae mita
def main():
    N, K, C = map(int, input().split())
    S = input()
    l = [0] * N
    r = [0] * N
    j = K+1
    d = {}
    t = None
    for ii, v in enumerate(reversed(S)):
        i = N - ii - 1
        if v == 'x':
            continue
        if t is None or t - C > i:
            j -= 1
            r[i] = j
            t = i
    if j <= 0:
        return
    t = None
    j = 0
    for i, v in enumerate(S):
        if v == 'x':
            continue
        if t is None or t + C < i:
            j += 1
            l[i] = j
            t = i
    if j > K:
        return
    rr = []
    for i in range(N):
        if r[i] > 0 and r[i] == l[i]:
            rr.append(i+1)
    for i in rr:
        print(i)
main()
