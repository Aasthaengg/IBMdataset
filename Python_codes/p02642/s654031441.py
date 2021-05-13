n = int(input())
aas = sorted(list(map(int, input().split())))
aas_len = len(aas)
if aas_len == 1:
    print(1)
    exit()
aas_max = aas[-1]
arr = [1]*(aas_max+1)
for i in range(aas_len):
    if arr[aas[i]] == 0:
        continue
    if arr[aas[i]] == 1:
        arr[aas[i]] = 2
    else:
        arr[aas[i]] = 0
        continue
    idx = aas[i]*2
    while idx <= aas_max:
        arr[idx] = 0
        idx += aas[i]
res = 0
for i in aas:
    if arr[i] != 0:
        res += 1
print(res)