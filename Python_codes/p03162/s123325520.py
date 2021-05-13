N = int(input())
prev_a = 0
prev_b = 0
prev_c = 0

for n in range(N):
    a, b, c = [int(i) for i in input().split(' ')]

    next_a = a + max(prev_b, prev_c)
    next_b = b + max(prev_a, prev_c)
    next_c = c + max(prev_a, prev_b)

    prev_a = next_a
    prev_b = next_b
    prev_c = next_c

print(max(prev_a, prev_b, prev_c))
