n = int(input())
t = 1
a = 1
for i in range(n):
    next_t, next_a = map(int, input().split())
    kake_t = (t + next_t - 1) // next_t
    kake_a = (a + next_a - 1) // next_a
    kake = max(kake_t, kake_a)
    t = next_t * kake
    a = next_a * kake
print(int(a + t))