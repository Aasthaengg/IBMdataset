s = input()
ls = len(s)

cnt = {"a": 0, "b": 0, "c": 0}

for i in s:
    cnt[i] += 1

ab = abs(cnt["a"] - cnt["b"])
ac = abs(cnt["a"] - cnt["c"])
bc = abs(cnt["b"] - cnt["c"])

f = (ab <= 1) and (ac <= 1) and (bc <= 1)

print("YES" if f else "NO")
