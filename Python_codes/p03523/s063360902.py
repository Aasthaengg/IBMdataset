from itertools import product


S = input()
chars = ["KIH", "B", "R", ""]
for As in product(["", "A"], repeat=4):
    cand = "".join(a + c for a, c in zip(As, chars))
    if cand == S:
        print("YES")
        break
else:
    print("NO")
