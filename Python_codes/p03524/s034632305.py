from collections import Counter
S = input()

cnt = Counter(S)

if max(cnt["a"], cnt["b"], cnt["c"]) - min (cnt["a"], cnt["b"], cnt["c"]) >= 2:
    print("NO")
else:
    print("YES")
