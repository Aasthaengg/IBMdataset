n,k,*aa = map(lambda x:int(x)-1, open(0).read().split())
n += 1
k += 1
passed = set()

i = 0
while k and i not in passed:
    k -= 1
    passed.add(i)
    i = aa[i]

if k:
    fst = i
    cycle = [fst]
    i = aa[i]

    while i != fst:
        cycle.append(i)
        i = aa[i]
    ans = cycle[k%len(cycle)]
else:
    ans = i
print(ans+1)