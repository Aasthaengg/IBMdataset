A, B, C, D, E, F = map(int, input().split())

best_dense = -float("inf")
for a in range(31):
    for b in range(31):
        for c in range(1501):
            for d in range(1501):
                w_sum = 100 * A * a + 100 * B * b
                s_sum = C * c + D * d
                sum = w_sum + s_sum
                if sum > F: break
                if w_sum == 0: break
                if E * (w_sum / 100) < s_sum: break
                dense = s_sum / sum
                if dense > best_dense:
                    best_dense = dense
                    ans_sum = sum
                    ans_s_sum = s_sum
print(ans_sum, ans_s_sum)
