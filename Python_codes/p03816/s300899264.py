n = int(input())
aas = list(map(int, input().split()))
max_n = max(aas) + 1
cnts = [0]*(max_n)
for i in aas:
    cnts[i] += 1
res = 0
for i in range(max_n):
    if cnts[i] != 0:
        cnts[i] -= 1
    if cnts[i]%2 == 0:
        cnts[i] = 0
    elif cnts[i] >= 3:
        cnts[i] = 1
res = len(set(aas))
adj = sum(cnts)
print(res if adj == 0 else res-(adj%2!=0))