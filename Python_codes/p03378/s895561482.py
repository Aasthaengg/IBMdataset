N, M, X = map(int, input().split())
L = list( map(int, input().split()) )

u = [i for i in L if i < X]
o = [i for i in L if i > X]
print(min(len(u), len(o)))