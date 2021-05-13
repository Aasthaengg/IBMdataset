MARCH = list('MARCH')
# print(MARCH)
N = int(input())
S = [input() for _ in range(N)]
# print(S)

namect = []
for i in range(5):
    st = [s for s in S if s.startswith(MARCH[i])]
    namect.append(len(st))
ans = 0
for i in range(5):
    for j in range(i+1, 5):
        for k in range(j+1, 5):
            ans += namect[i]*namect[j]*namect[k]
print(ans)
