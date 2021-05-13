N, M, X, Y = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
flg = False
for Z in range(-100,101):
    if X<Z<=Y and max(A)<Z and min(B) >= Z:
        flg = True
if flg:
    print("No War")
else:
    print("War")