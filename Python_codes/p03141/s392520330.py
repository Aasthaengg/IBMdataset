N = int(input())
l = []
for i in range(N):
    A, B = [int(_c) for _c in input().split(" ")]
    l.append({"A": A, "B": B, "sum": A + B})

l = sorted(l, key=lambda x: x["sum"], reverse=True)

a_total = 0
b_total = 0
for i, _l in enumerate(l):
    if i % 2 == 0:
        a_total += _l["A"]
    else:
        b_total += _l["B"]

print(a_total - b_total)