a, b, x = map(int, input().split())
ans_b = 1
ans_a = 1
ans_b += b // x
ans_a += a // x
if a % x == 0:
    print(ans_b-ans_a + 1)
else:
    print(ans_b-ans_a)
