import itertools
N = int(input())
dic = [0 for _ in range(5)]
for i in range(N):
    S = input()
    data = S[0]
    if data == "M":  dic[0] += 1
    if data == "A":  dic[1] += 1
    if data == "R":  dic[2] += 1
    if data == "C":  dic[3] += 1
    if data == "H":  dic[4] += 1
    
a = range(5)
comb = list(itertools.combinations(a, 3))

ans = 0
for c in comb:
    ans += dic[c[0]] * dic[c[1]] * dic[c[2]]
print(ans)