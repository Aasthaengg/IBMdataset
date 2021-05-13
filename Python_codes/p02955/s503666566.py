from itertools import accumulate

def divisors(n):
    divs = []
    for i in range(1, int(n ** 0.5) + 1):
        d, m = divmod(n, i)
        if m == 0:
            divs.append(i)
            divs.append(d)
    divs.sort(reverse=True)
    return divs

n, k = map(int, input().split())
a = list(map(int, input().split()))
divs = divisors(sum(a))

for div in divs:
    m = [ x % div for x in a ]
    m.sort()
    l = [0] + list(accumulate(m))
    r = list(reversed([0] + list(accumulate(reversed([div - x for x in m])))))
    for i in range(len(l)):
        if l[i] == r[i]:
            if l[i] <= k:
                print(div)
                exit()
            break
        elif l[i] > r[i]:
            break