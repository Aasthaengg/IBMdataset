#C
N,M,D = map(int,input().split())
if D != 0:
    ans = (M-1)*(1/N)*(1/N)*2*(N-D)
else:
    ans = (M-1)*(1/N)
print(ans)

