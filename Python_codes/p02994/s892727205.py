N,L = map(int,input().split())

l = [i+L for i in range(N)]
_l= [abs(x) for x in l]
l_min_id = _l.index(min(_l))
print(sum(l)-l[l_min_id])