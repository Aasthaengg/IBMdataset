from itertools import product
from functools import lru_cache
n = int(input())
mod = 10**9+7
condition = True

@lru_cache(64*n)
def func(tpl, count) :
    if tpl in (("A","G","C"), ("A","C","G"), ("G","A","C")) :
        return 0
    if count :
        count -= 1
        if tpl[1:] == ("A","G") :
            return sum(func(("A","G",c), count) for c in "AGT")%mod
        if tpl[1:] == ("A","C") :
            return sum(func(("A","C",c), count) for c in "ACT")%mod
        if tpl[1:] == ("G","A") :
            return sum(func(("G","A",c), count) for c in "AGT")%mod
        if tpl[:2] == ("A","G") :
            return sum(func(tpl[1:]+(c,), count) for c in "AGT")%mod
        if tpl[0]+tpl[2] == "AG" :
            return sum(func(tpl[1:]+(c,), count) for c in "AGT")%mod
        return sum(func(tpl[1:]+(c,), count) for c in "ACGT")%mod
    return 1

ans = 0
for firstthree in product("ACGT", repeat=3) :
    ans = (ans+func(firstthree, n-3))%mod
print(ans)