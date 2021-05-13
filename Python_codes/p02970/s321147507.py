N,D = map(int, input().split())
D = 2*D + 1
k = N/D
l = N//D
if k == l:
    print(int(k))
else:
    print(l+1)