N,A,B = map(int,input().split())
_max = min(A,B)
_min = min(A,B) - (N - max(A,B))
if _min < 0:
    _min = 0
print(_max,_min)