N, M = map(int, input().split())

wa_num = 0
ac_num = 0

WA = [0] * N
AC = [False] * N

for _ in range(M):
    p, S = input().split()
    p = int(p) - 1

    if AC[p]:
        continue

    if S == "AC":
        AC[p] = True
        ac_num += 1
        wa_num += WA[p]
    elif S == "WA":
        WA[p] += 1

print(f"{ac_num} {wa_num}")
