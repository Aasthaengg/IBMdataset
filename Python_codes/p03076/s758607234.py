def order(n):
    if n == 0: return 10
    else: return n


def ceil(num, target):
    if num % target == 0: return num
    return ((int)(num / target) + 1) * target


P = [input() for _ in range(5)]
P_sorted = sorted(P, key=lambda pi: order(int(pi[-1])), reverse=True)

ans = 0
for pi in P_sorted[:-1]:
    ans += ceil(int(pi), 10)

print(ans + int(P_sorted[-1]))