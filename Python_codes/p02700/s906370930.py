
A, B, C, D = map(int, input().split())
tk_count = C//B if C%B==0 else C//B + 1
ao_count = A//D if A%D==0 else A//D + 1
if tk_count <= ao_count:
    print('Yes')
else:
    print('No')


