#ABC 068

N = int(input())
ls = []
for i in range(0,8):
    ls.append(2**i)

ans = 0
for x in range(len(ls)):
    if ls[x] <= N:
        ans = ls[x]
print(ans)