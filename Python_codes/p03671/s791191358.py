price_of_bell_a, price_of_bell_b, price_of_bell_c = map(int, input().split())

sum_a_b = price_of_bell_a + price_of_bell_b
sum_a_c = price_of_bell_a + price_of_bell_c
sum_b_c = price_of_bell_b + price_of_bell_c

print(min(sum_a_b, sum_a_c, sum_b_c))