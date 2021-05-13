N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()
L = [0]*N
dic = dict()
dic["r"] = P
dic["s"] = R
dic["p"] = S
dic["0"] = 0
res = 0
for i in range(N):
    if i < N-K and T[i] == T[i+K] and L[i] == 0:
        L[i+K] = 1
    if L[i] == 0:
        res += dic[T[i]]
print(res)