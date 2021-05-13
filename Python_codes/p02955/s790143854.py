from itertools import accumulate
N, K = map(int, input().split())
A = list(map(int, input().split()))


A_sum = sum(A)
ans_candidates = []
for n in range(1, int(A_sum ** 0.5) + 1):
    if A_sum % n == 0:
        ans_candidates.append(n)
        ans_candidates.append(A_sum // n)
ans_candidates.sort(reverse=True)


for z in ans_candidates:
    need_add = [(z - a % z) % z for a in A]
    need_add.sort()
    need_minus = [z - na for na in need_add]

    need_add = list(accumulate(need_add))
    need_minus = list(accumulate(need_minus))

    for i in range(N):
        if (need_add[i] == need_minus[-1] - need_minus[i]) and (need_add[i] <= K):
            print(z)
            exit()
