N, M, X = list(map(int, input().split()))
A = list(map(int, input().split()))

Ncnt = [i for i in A if i>X]
Zcnt = [i for i in A if i<X]
print(min(len(Ncnt), len(Zcnt)))