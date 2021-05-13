from itertools import combinations

n = int(input())
c = [0, 0, 0, 0, 0]

indices = [0, 1, 2, 3, 4]
letters = ["M", "A", "R", "C", "H"]
mapping = dict(zip(letters, indices))

for i in range(n):
    s = input()
    if s[0] in mapping:
        c[mapping[s[0]]] += 1

cnt = 0
for combo in combinations(c, 3):
    cnt += combo[0]*combo[1]*combo[2]

print(cnt)