quantity_a, filled_a, filled_b = map(int, input().split())

sum_a_b = filled_a + filled_b

if quantity_a >= sum_a_b:
    print(0)
else:
    print(sum_a_b - quantity_a)