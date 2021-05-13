#辞書型でリトライ
N,K = map(int, input().split(' '))
A = input().split(' ')

dic = {}
for a in range(len(A)):
    tmp = A[a]
    if not tmp in dic:
        dic[tmp] = 1
    else:
        dic[tmp] += 1

values = sorted(dic.values())
ans = 0
if len(values)<=K:
    pass
else:
    tmp = len(values)-K
    values = values[:tmp]
    ans = sum(values)

print(ans)