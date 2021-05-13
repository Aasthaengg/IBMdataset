S = input()
lenS = len(S)
ans = 0
def f(SUM,TMP,N):
    n = int(S[N])
    if N == lenS-1:
        SUM += TMP + n
        return SUM
    else:
        ret = f(SUM,(TMP+n)*10,N+1) + f(SUM+TMP+n,0,N+1)
        return ret

print(f(0,0,0))
