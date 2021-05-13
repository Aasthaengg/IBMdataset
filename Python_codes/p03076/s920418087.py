a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
import itertools

kouho = list(itertools.permutations([a, b, c, d, e]))
ans = 10 ** 6
for k in kouho:
    temp = 0
    for t in range(5):
        amari = k[t] % 10
        if amari != 0 and t != 4:
            temp += 10 - amari
        temp += k[t]
    ans = min(ans, temp)
print(ans)
