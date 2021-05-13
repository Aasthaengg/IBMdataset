from itertools import product

def solve(NUM, LIST):
    lst = [l[i] for i, li in enumerate(LIST) if li == NUM]
    if len(lst) == 0:
        return 10 ** 5
    ANS = (len(lst) - 1) * 10
    ANS += abs(sum(lst) - target[NUM])
    return ANS

target = list(map(int, input().split()))
l = [int(input()) for _ in range(target[0])]

ans = 10 ** 5
for pat in product([0, 1, 2, 3], repeat=target[0]):
    tmp = sum(solve(i + 1, pat) for i in range(3))
    ans = min(ans, tmp)
print(ans)
