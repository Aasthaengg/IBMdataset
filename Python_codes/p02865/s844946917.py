def f(N):
    if N%2==0:
        return N//2-1
    else:
        return N//2
N=int(input())
print(f(N))