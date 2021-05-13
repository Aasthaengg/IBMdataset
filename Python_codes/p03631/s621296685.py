n = list(str(input()))
n_r = [ i for i in reversed(n)]
if n == n_r:
    print('Yes')
else:
    print('No')