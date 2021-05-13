# N：人数 M：種類
# K1：個 A1 A2 ...：好きな食べ物の数字
# K2 A1 A2
# 全員が好きな食べ物の種類数

N, M = map(int, input().split())
s = set(range(1, M+1))

for _ in range(N):
    k, *a = map(int, input().split())
    s&=set(a)
print(len(s))