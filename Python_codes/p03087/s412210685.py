from itertools import accumulate
N, Q = map(int,input().split())
S = input()
A = [list(map(int,input().split())) for q in range(Q)]
#print(A)

#フラグを立てて累積和で高速化
flg = []
for n in range(N-1):
    tmp_s = S[n:n+2]
    if tmp_s == "AC":
        flg.append(1)
    else:
        flg.append(0)

flg2 = [0] + flg
flg2 = list(accumulate(flg2))
#print(flg2)

for a in A:
    print(flg2[a[1]-1] - flg2[a[0]-1])