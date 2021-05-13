import math
def divisors(n, sort=True, reverse=False):
    sqn = math.sqrt(n)
    sqn_int = int(sqn)
    div_list = []
    if sqn == sqn_int:
        div_list.append(sqn_int)
        loop = range(1,sqn_int)
    else:
        loop = range(1,sqn_int + 1)
    for i in loop:
        if n % i == 0:
            div_list.append(i)
            div_list.append(n//i)
    if sort:
        div_list.sort(reverse=reverse)
    return div_list

inpl = lambda: list(map(int,input().split()))
N, K = inpl()
A = inpl()
S = sum(A)
div = divisors(S, reverse=True)
for d in div:
    mods = [ a % d for a in A ]
    mods.sort()
    Sm = sum(mods)
    h = Sm // d
    minK = min(d*(h+1) - sum(mods[N-h-1:]), sum(mods[:N-h]))
    if minK <= K:
        print(d)
        break