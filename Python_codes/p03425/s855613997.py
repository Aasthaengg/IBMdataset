from itertools import combinations

N = int(input())
cnt = {"M": 0, "A": 0, "R": 0, "C": 0, "H": 0}
for _ in range(N):
    s = input()
    if s[0] == "M":
        cnt["M"] += 1
    elif s[0] == "A":
        cnt["A"] += 1
    elif s[0] == "R":
        cnt["R"] += 1
    elif s[0] == "C":
        cnt["C"] += 1
    elif s[0] == "H":
        cnt["H"] += 1

comb = combinations(["M", "A", "R", "C", "H"], 3)
# print(list(comb))

ans = 0
for c in comb:  # 計10通り
    ans += cnt[c[0]] * cnt[c[1]] * cnt[c[2]]

print(ans)
