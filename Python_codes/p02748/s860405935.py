a_b_m_var = input().split()
a_i_var = input().split()
b_i_var = input().split()

a_b_m = [int(s) for s in a_b_m_var]
a_i = [int(s) for s in a_i_var]
b_i = [int(s) for s in b_i_var]

not_discount_price = min(a_i) + min(b_i)

down_price_i = []
for i in range(a_b_m[2]):
    price_down_var = input().split()
    price_down = [int(s) for s in price_down_var]
    a, b, m = price_down[0], price_down[1], price_down[2]
    price = a_i[a-1] + b_i[b-1] - m
    down_price_i.append(price)

if not_discount_price > min(down_price_i):
    print(min(down_price_i))
else:
    print(not_discount_price)