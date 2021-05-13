N, M = list(map(int, input().split()))

is_solved = [False] * N
wa_count = [0] * N
wa_total = 0

for _ in range(M):
    p, s = list(input().split())
    p = int(p) - 1

    if s == 'AC':
        if not is_solved[p]:
            is_solved[p] = True
            wa_total += wa_count[p]
    else:
        wa_count[p] += 1

print(sum(is_solved), wa_total)