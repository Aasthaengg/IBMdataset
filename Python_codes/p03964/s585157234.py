import math
N = int(input())

t = 0
a = 0
for i in range(N):
    T, A = map(int, input().split())
    if i == 0:
        t += T
        a += A
        continue
    if (T >= t and A >= a):
        t = T
        a = A
        continue

    max_ta = max(t, a)
    g = math.gcd(t, a)
    tg, ag = t // g, a // g
    if (T, A) != (tg, ag):
        sum_t, sum_a = T * max_ta, A * max_ta
        # print(sum_t, sum_a)

        cout_sn = min((sum_t - t) // T, (sum_a - a) // A)
        # while True:
        sum_t -= T * cout_sn
        sum_a -= A * cout_sn
        # if sum_t < t or sum_a < a:
        #     sum_t += T
        #     sum_a += A
        #     break
        t = sum_t
        a = sum_a
        continue

print(t + a)
