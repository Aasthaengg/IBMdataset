n = int(input())

li_ans = [0] * n

for a in range(1, 110):
    for b in range(1, 110):
        for c in range(1, 110):
            val = (a ** 2) + (b ** 2) + (c ** 2) + (a * b) + (b * c) + (c * a)
            if val <= n:
                li_ans[val - 1] += 1
for an in li_ans:
    print(an)
