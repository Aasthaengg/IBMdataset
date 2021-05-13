n=int(input())
MAX_N=n
X = [None] * (MAX_N + 1)
def f(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if X[n]:
        return X[n]
    r=f(n-1)+f(n-2)
    X[n]=r
    return r
print(f(n))
