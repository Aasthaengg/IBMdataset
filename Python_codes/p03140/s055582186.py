N=int(input())
def f(a,b,c):
    X=sorted([a,b,c])
    if a==b==c:
        return 0
    elif X[0]==X[1] or X[1]==X[2]:
        return 1
    else:
        return 2
print(sum(f(a,b,c) for a,b,c in zip(input(),input(),input())))