N, M, X = map(int, input().split())
A = list(map(int, input().split()))

mae = [i for i in A if i > X]
ushiro = [i for i in A if i < X]
m = len(mae)
u = len(ushiro)

if m > u:
    print(u)
else:
    print(m)