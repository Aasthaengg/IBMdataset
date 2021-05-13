import sys
sys.setrecursionlimit(10**7)

N = int(input())
H = list(map(int, input().split()))


def need(L):
    if L == [] or max(L) == 0:
        return 0
    if min(L) > 0:
        l = [L[i]-1 for i in range(len(L))]
        return need(l)+1
    else:
        i = L.index(0)
        l = L[:i]
        m = L[i+1:]
        return need(l)+need(m)


print(need(H))
