N, P = map(int, input().split())
A = list(map(int, input().split()))

dic = {"even":0, "odd":0}
for i in range(N):
    if A[i] % 2 == 0:
        dic["even"] += 1
    else:
        dic["odd"]  += 1

if dic["odd"] == 0:
    if P == 1:
        print(0)
    else:
        print(2 ** dic["even"])

else:
    print(2 ** (N-1))