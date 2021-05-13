n = int(input())
s = input()

rinds, ginds, binds = [], [], []

for i in range(n):
    if s[i] == 'R': rinds.append(i)
    elif s[i] == 'G': ginds.append(i)
    else: binds.append(i)


rlen, glen, blen = len(rinds), len(ginds), len(binds)

def binsearch_same(binds, blen, dist, i):
    lo, hi = 0, blen-1
    while lo<=hi:
        mid = lo + (hi-lo)//2
        d = binds[mid] - i
        if dist == d:
            return True
        elif d < dist:
            lo = mid + 1
        else:
            hi = mid - 1
    return False

ans = 0

for i in rinds:
    for j in ginds:
        dist = abs(i-j)
        i_ = min(i, j)
        j_ = max(i, j)
        ans += blen
        # i' < j' < k

        if binsearch_same(binds, blen, dist, j_):
            ans -= 1
        # i'< k < j' 
        if dist%2==0 and binsearch_same(binds, blen, dist//2, i_):
            ans -= 1
        # # k < i' < j'
        if binsearch_same(binds, blen, -dist, i_):
            ans -= 1

print(ans)




