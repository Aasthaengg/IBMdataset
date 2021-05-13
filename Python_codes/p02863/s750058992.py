N,T = map(int,input().split())
AB = [tuple(map(int,input().split())) for i in range(N)]

dp0 = {0:0}
dp1 = {0:0}

for i,(a,b) in enumerate(AB):
    _dp0 = {0:0}
    _dp1 = {0:0}
    for k0,v0 in dp0.items():
        if k0 in _dp0:
            _dp0[k0] = max(_dp0[k0], v0)
        else:
            _dp0[k0] = v0
        if k0+a < T:
            if k0+a in _dp0:
                _dp0[k0+a] = max(_dp0[k0+a], v0+b)
            else:
                _dp0[k0+a] = v0+b
        if k0 in _dp1:
            _dp1[k0] = max(_dp1[k0], v0+b)
        else:
            _dp1[k0] = v0+b
    for k1,v1 in dp1.items():
        if k1 in _dp1:
            _dp1[k1] = max(_dp1[k1], v1)
        else:
            _dp1[k1] = v1
        if k1+a < T:
            if k1+a in _dp1:
                _dp1[k1+a] = max(_dp1[k1+a], v1+b)
            else:
                _dp1[k1+a] = v1+b
    dp0 = _dp0
    dp1 = _dp1

print(max(dp1.values()))