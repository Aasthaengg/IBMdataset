n = int(input())
votes = [list(map(int, input().split())) for _ in range(n)]

curr_a, curr_b = 0, 0

for v1, v2 in votes:
    a, b = v1, v2
    i = max(curr_a // v1, curr_b // v2)

    while a < curr_a or b < curr_b:
        a = v1 * i
        b = v2 * i
        i += 1

    curr_a, curr_b = a, b

print(curr_a + curr_b)
