D = int(input())
C = list(map(int, input().split()))
S = list()
for i in range(D):
    tmp_ = list(map(int, input().split()))
    S.append(tmp_)
T = list()
for i in range(D):
    T.append(int(input()))
ret = 0
lastd = [0] * 26
for i in range(D):
    ret += S[i][T[i]-1]
    lastd[T[i] - 1] = i + 1
    for j in range(26):
        ret -= C[j] * (i + 1 - lastd[j])
    print(ret)